from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


class Configuration:

    @classmethod
    def start_url(cls):
        return JsonSettingsFile("config.json", RootPathHelper.current_root_path(__file__)).get("startUrl")
