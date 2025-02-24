import logging
import pytest
import os
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from _pytest.fixtures import FixtureRequest
from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.logging.logger import Logger
from integration_template.browsers.custom_startup import CustomStartup
from datetime import datetime
from integration_template.database.mysql_database import MySQLDatabase
from integration_template.configurations.configuration import Configuration
from integration_template.models.author_model import AuthorModel
from integration_template.models.project_model import ProjectModel
from integration_template.models.status_model import StatusModel
from integration_template.models.session_model import SessionModel
from integration_template.models.test_model import TestModel


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)
    Logger.info(f'Setting work_dir: {work_dir}')

    for log_name in [
        "selenium.webdriver.remote.remote_connection",
        "selenium.webdriver.common.selenium_manager",
        "urllib3.connectionpool",
    ]:
        logger = logging.getLogger(log_name)
        logger.disabled = True

    Logger.info("Setup startup config")
    BrowserServices.Instance.set_startup(CustomStartup())
    lst = []
    yield lst


@pytest.fixture(scope="function", autouse=True)
def setup_function(request: FixtureRequest):
    BrowserServices.Instance.browser.maximize()
    yield
    if BrowserServices.Instance.is_browser_started:
        Logger.info("Closing browser")
        BrowserServices.Instance.browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    report = (yield).get_result()
    if not getattr(item, 'report', None) or not report.passed:
        setattr(item, 'report', report)


@pytest.fixture(scope="function")
def get_new_record(request: FixtureRequest):
    if MySQLDatabase().is_field_in_table(AuthorModel().table_name,
                                         AuthorModel().column_name,
                                         Configuration().get_config_data().author.name) is False:
        MySQLDatabase().insert_record(Configuration().get_config_data().author.model_dump(),
                                      AuthorModel().table_name)

    if MySQLDatabase().is_field_in_table(ProjectModel().table_name,
                                         ProjectModel().column_name,
                                         Configuration().get_config_data().project.name) is False:
        MySQLDatabase().insert_record(Configuration().get_config_data().project.model_dump(),
                                      ProjectModel().table_name)
    yield
    new_instance = {'name': request.node.report.nodeid,
                    'status_id': MySQLDatabase().get_id_from_table_by_column_name(
                        StatusModel().table_name,
                        StatusModel().column_name,
                        request.node.report.outcome),
                    'method_name': request.node.name,
                    'project_id': MySQLDatabase().get_id_from_table_by_column_name(
                        ProjectModel().table_name,
                        ProjectModel().column_name,
                        Configuration().get_config_data().project.name),
                    'session_id': MySQLDatabase().get_id_from_table_by_column_name(
                        SessionModel().table_name,
                        SessionModel().column_name,
                        Configuration().get_config_data().session),
                    'start_time': datetime.fromtimestamp(request.node.report.start),
                    'end_time': datetime.fromtimestamp(request.node.report.stop),
                    'env': Configuration().get_config_data().env,
                    'browser': BrowserServices.Instance.browser.browser_name,
                    'author_id': MySQLDatabase().get_id_from_table_by_column_name(
                        AuthorModel().table_name,
                        AuthorModel().column_name,
                        Configuration().get_config_data().author.name)
                    }
    MySQLDatabase().insert_record(new_instance,
                                  TestModel().table_name)
    global record_id
    record_id = MySQLDatabase().get_last_insert_record_id(TestModel().table_name)


@pytest.fixture(scope="function")
def get_copy_record(request: FixtureRequest, id: int):
    yield
    MySQLDatabase().copy_record_by_id(id,
                                      TestModel().table_name,
                                      MySQLDatabase().get_id_from_table_by_column_name(
                                          AuthorModel().table_name,
                                          AuthorModel().column_name,
                                          Configuration().get_config_data().author.name),
                                      MySQLDatabase().get_id_from_table_by_column_name(
                                          ProjectModel().table_name,
                                          ProjectModel().column_name,
                                          Configuration().get_config_data().project.name))
    new_record_id = MySQLDatabase().get_last_insert_record_id(TestModel().table_name)
    new_status = request.node.report.outcome
    MySQLDatabase().update_record_by_id(new_record_id,
                                        TestModel().table_name,
                                        TestModel().column_name,
                                        MySQLDatabase().get_id_from_table_by_column_name(
                                            StatusModel().table_name,
                                            StatusModel().column_name,
                                            new_status
                                            )
                                        )


@pytest.hookimpl()
def pytest_sessionfinish(session):
    MySQLDatabase().delete_record_by_condition(TestModel().table_name,
                                               TestModel().condition,
                                               [record_id])
    MySQLDatabase().closing_connection()
