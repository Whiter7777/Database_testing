import autoit
from pathlib import Path
from py_selenium_auto_core.utilities.file_reader import FileReader
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


class UploadFile:
    @staticmethod
    def upload_file_to_explorer():
        id_explorer_open = "[CLASS:#32770]"
        id_input_line = "[CLASS:Edit; INSTANCE:1]"
        id_open_button = "Button1"
        file_name = "file_to_upload.jpg"
        test_file = FileReader.get_resource_file_path(
            str(Path("test_data", file_name)),
            RootPathHelper.calling_root_path(),
        )
        autoit.win_wait_active(id_explorer_open, 5)
        autoit.control_set_text(id_explorer_open, id_input_line, test_file)
        autoit.control_click(id_explorer_open, id_open_button)
