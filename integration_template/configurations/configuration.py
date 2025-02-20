from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from integration_template.models.config_model import ConfigModel
from integration_template.utilities.deserialize_json import DeserializeJson
import os
from pathlib import Path


class Configuration:
    _BASE_DIR = RootPathHelper.current_root_path(__file__)
    _config_file_path = Path(
        os.path.join(_BASE_DIR, "./resources", "config.json")
    ).resolve()

    @classmethod
    def start_url(cls):
        return JsonSettingsFile("config.json", RootPathHelper.current_root_path(__file__)).get("startUrl")

    @classmethod
    def get_config_data(cls):
        return ConfigModel.model_validate_json(DeserializeJson().deserialize_json(cls._config_file_path))
