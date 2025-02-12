from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from integration_template.utilities.get_random_data import GetRandomData
from py_selenium_auto.elements.check_box import CheckBox


class AvatarForm(Form):
    def __init__(self):
        super().__init__(Locator(By.CLASS_NAME, "avatar-and-interests-page"), "Avatar Form")
        self.upload_button = self._element_factory.get_button(
            Locator(By.CLASS_NAME, "avatar-and-interests__upload-button"),
            "Upload Button")
        self.upload_text = self._element_factory.get_text_box(
            Locator(By.CLASS_NAME, "avatar-and-interests__text"),
            "Upload Text")
        self.unselect_checkbox = self._element_factory.get_check_box(
            Locator(By.XPATH, "//*[@for='interest_unselectall']"),
            "Unselect Checkbox")
        self.next_button = self._element_factory.get_button(
            Locator(By.XPATH, "//button[text()='Next']"),
            "Next Button")

    def is_page_displayed(self):
        return self.state.is_displayed()

    def attach_file(self):
        self.upload_button.click()

    def check_random_checkboxes(self, num_of_select: int):
        self.unselect_checkbox.click()
        checkbox_list = self._element_factory.find_elements(
            CheckBox,
            Locator(By.XPATH,
                    "//*[@class='checkbox__label' and (@for!='interest_unselectall' and @for!='interest_selectall')]"),
            "Checkbox List"
        )
        random_num_list = GetRandomData().generate_random_numbers(len(checkbox_list), num_of_select)
        for i in random_num_list:
            checkbox_list[i].click()

    def click_next_button(self):
        if self.next_button.state.is_enabled():
            self.next_button.click()
