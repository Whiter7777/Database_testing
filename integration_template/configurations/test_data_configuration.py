from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


class TestDataConfiguration:

    @classmethod
    def get_email(cls):
        return JsonSettingsFile("test_data.json", RootPathHelper.current_root_path(__file__)).get("email")

    @classmethod
    def get_domain(cls):
        return JsonSettingsFile("test_data.json", RootPathHelper.current_root_path(__file__)).get("domain")

    @classmethod
    def get_timer(cls):
        return JsonSettingsFile("test_data.json", RootPathHelper.current_root_path(__file__)).get("timer")
