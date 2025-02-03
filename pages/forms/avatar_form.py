from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from integration_template.utilities.random_num_generator import RandomNumGenerator
from pathlib import Path
from py_selenium_auto_core.utilities.file_reader import FileReader
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from py_selenium_auto.elements.check_box import CheckBox
import autoit


class AvatarForm(Form):
    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[@class='avatar-and-interests-page']"), "Avatar Form")
        self.upload_button = self._element_factory.get_button(
            Locator(By.XPATH, "//*[@class='avatar-and-interests__upload-button']"),
            "Upload Button")
        self.upload_text = self._element_factory.get_text_box(
            Locator(By.XPATH, "//*[@class='avatar-and-interests__text']"),
            "Upload Text")
        self.unselect_checkbox = self._element_factory.get_check_box(
            Locator(By.XPATH, "//*[@for='interest_unselectall']"),
            "Unselect Checkbox")
        self.next_button = self._element_factory.get_button(
            Locator(By.XPATH, "//button[text()='Next']"),
            "Next Button")

    def page_is_displayed(self):
        return self.state.is_displayed()

    def attach_file(self):
        id_explorer_open = "[CLASS:#32770]"
        id_input_line = "[CLASS:Edit; INSTANCE:1]"
        id_open_button = "Button1"
        file_name = "file_to_upload.jpg"
        test_file = FileReader.get_resource_file_path(
            str(Path("test_data", file_name)),
            RootPathHelper.calling_root_path(),
        )
        self.upload_button.click()
        autoit.win_wait_active(id_explorer_open, 5)
        autoit.control_set_text(id_explorer_open, id_input_line, test_file)
        autoit.control_click(id_explorer_open, id_open_button)

    # def check_unselect_checkbox(self):
    #     if self.unselect_checkbox.check():
    #         self.unselect_checkbox.click()

    def check_random_checkboxes(self):
        if self.unselect_checkbox.check():
            self.unselect_checkbox.click()
        checkbox_list = self._element_factory.find_elements(
            CheckBox,
            Locator(By.XPATH,
                    "//*[@class='checkbox__label' and (@for!='interest_unselectall' and @for!='interest_selectall')]"),
            "Checkbox List"
        )
        random_num_list = RandomNumGenerator().generate_random_numbers(len(checkbox_list))
        for i in random_num_list:
            checkbox_list[i].click()

    def click_next_button(self):
        if self.next_button.state.is_enabled():
            self.next_button.click()
