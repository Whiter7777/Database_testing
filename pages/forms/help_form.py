from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class HelpForm(Form):
    def __init__(self):
        super().__init__(Locator(By.CLASS_NAME, "help-form"), "Help Form")
        self.send_to_bottom_button = self._element_factory.get_button(
            Locator(By.XPATH, "//*[contains(@class, 'help-form__send-to-bottom-button')]"),
            "Send to bottom button"
        )
        self.help_form_hidden = self._element_factory.get_label(
            Locator(By.XPATH, "//*[@class='help-form is-hidden']"),
            "Help Form is hidden")

    def is_page_displayed(self):
        return self.state.is_displayed()

    def click_send_to_bottom_button(self):
        if self.send_to_bottom_button.state.is_enabled():
            self.send_to_bottom_button.click()

    def is_help_form_hidden(self):
        return self.help_form_hidden.state.wait_for_displayed()
