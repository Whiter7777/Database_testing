from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from integration_template.models.testing_model import TestUserInterfaceModel
from integration_template.utilities.deserialize_json import DeserializeJson
import os
from pathlib import Path


class TestDataConfiguration:
    _BASE_DIR = RootPathHelper.current_root_path(__file__)
    _config_file_path = Path(
        os.path.join(_BASE_DIR, "./resources", "test_data.json")
    ).resolve()

    @classmethod
    def get_test_data(cls):
        return TestUserInterfaceModel.model_validate_json(DeserializeJson().deserialize_json(cls._config_file_path))
