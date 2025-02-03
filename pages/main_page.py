from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class MainPage(Form):
    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[contains(@class, 'start view')]"), "Main Page")
        self.next_page_button = self._element_factory.get_button(
            Locator(By.XPATH, "//*[@class='start__link']"),
            "Next Page Button")

    def page_is_displayed(self):
        return self.state.is_displayed()

    def click_next_page_button(self):
        if self.next_page_button.state.is_enabled():
            self.next_page_button.click()
