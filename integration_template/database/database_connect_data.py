import configparser
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
import os
from pathlib import Path


class DBConnectData:
    @staticmethod
    def db_connect_data():
        config = configparser.ConfigParser()
        base_dir = RootPathHelper.current_root_path(__file__)
        config_file_path = Path(
            os.path.join(base_dir, "database/config.ini")
        ).resolve()

        config.read(config_file_path)
        host = config.get("Settings", "host")
        username = config.get("Settings", "username")
        password = config.get("Settings", "password")
        database = config.get("Settings", "database")
        return {"host": host, "username": username, "password": password, "database": database}
