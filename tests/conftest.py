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
from integration_template.configurations.testing_data_configuration import TestDataConfiguration


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
    if MySQLDatabase().is_field_in_table(TestDataConfiguration().get_test_data().author_table.table_name,
                                         TestDataConfiguration().get_test_data().author_table.column_name,
                                         Configuration().get_config_data().author.name) is False:
        MySQLDatabase().create_record(Configuration().get_config_data().author.model_dump(),
                                      TestDataConfiguration().get_test_data().author_table.table_name)

    if MySQLDatabase().is_field_in_table(TestDataConfiguration().get_test_data().project_table.table_name,
                                         TestDataConfiguration().get_test_data().project_table.column_name,
                                         Configuration().get_config_data().project.name) is False:
        MySQLDatabase().create_record(Configuration().get_config_data().project.model_dump(),
                                      TestDataConfiguration().get_test_data().project_table.table_name)
    yield
    new_instance = {'name': request.node.report.nodeid,
                    'status_id': MySQLDatabase().read_id_from_table_by_column_name(
                        TestDataConfiguration().get_test_data().status_table.table_name,
                        TestDataConfiguration().get_test_data().status_table.column_name,
                        request.node.report.outcome),
                    'method_name': request.node.name,
                    'project_id': MySQLDatabase().read_id_from_table_by_column_name(
                        TestDataConfiguration().get_test_data().project_table.table_name,
                        TestDataConfiguration().get_test_data().project_table.column_name,
                        Configuration().get_config_data().project.name),
                    'session_id': MySQLDatabase().read_id_from_table_by_column_name(
                        TestDataConfiguration().get_test_data().session_table.table_name,
                        TestDataConfiguration.get_test_data().session_table.column_name,
                        Configuration().get_config_data().session),
                    'start_time': datetime.fromtimestamp(request.node.report.start),
                    'end_time': datetime.fromtimestamp(request.node.report.stop),
                    'env': Configuration().get_config_data().env,
                    'browser': BrowserServices.Instance.browser.browser_name,
                    'author_id': MySQLDatabase().read_id_from_table_by_column_name(
                        TestDataConfiguration().get_test_data().author_table.table_name,
                        TestDataConfiguration().get_test_data().author_table.column_name,
                        Configuration().get_config_data().author.name)
                    }
    MySQLDatabase().create_record(new_instance,
                                  TestDataConfiguration().get_test_data().test_table.table_name)
    global record_id
    record_id = MySQLDatabase().read_last_insert_record_id(
        TestDataConfiguration().get_test_data().test_table.table_name)


@pytest.fixture(scope="function")
def get_copy_record(request: FixtureRequest, id: int):
    yield
    MySQLDatabase().copy_record_by_id(id,
                                      TestDataConfiguration().get_test_data().test_table.table_name,
                                      MySQLDatabase().read_id_from_table_by_column_name(
                                          TestDataConfiguration().get_test_data().author_table.table_name,
                                          TestDataConfiguration().get_test_data().author_table.column_name,
                                          Configuration().get_config_data().author.name),
                                      MySQLDatabase().read_id_from_table_by_column_name(
                                          TestDataConfiguration().get_test_data().project_table.table_name,
                                          TestDataConfiguration().get_test_data().project_table.column_name,
                                          Configuration().get_config_data().project.name))
    new_record_id = MySQLDatabase().read_last_insert_record_id(
        TestDataConfiguration().get_test_data().test_table.table_name)
    new_status = request.node.report.outcome
    MySQLDatabase().update_record_by_id(new_record_id,
                                        TestDataConfiguration().get_test_data().test_table.table_name,
                                        TestDataConfiguration().get_test_data().test_table.column_name,

                                        MySQLDatabase().read_id_from_table_by_column_name(
                                            TestDataConfiguration().get_test_data().status_table.table_name,
                                            TestDataConfiguration().get_test_data().status_table.column_name,
                                            new_status
                                            )
                                        )


@pytest.hookimpl()
def pytest_sessionfinish(session):
    MySQLDatabase().delete_record(TestDataConfiguration.get_test_data().test_table.table_name,
                                  TestDataConfiguration.get_test_data().test_table.condition,
                                  [record_id])
