from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class CookiesForm(Form):
    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[@class='cookies']"), "Cookies Form)")
        self.cookies_accept_button = self._element_factory.get_button(
            Locator(By.XPATH, "//*[contains(@class, 'button--transparent')]"),
            "Cookies Accept Button")

    def is_page_displayed(self):
        return self.state.wait_for_displayed()

    def accept_cookies(self):
        if self.cookies_accept_button.state.is_enabled():
            self.cookies_accept_button.click()

    def is_page_not_displayed(self):
        return self.state.wait_for_not_displayed()
