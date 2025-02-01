from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


# //*[@class = 'game view']
# "//*[contains(@class, 'start view')]"

class MainPage(Form):
    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[contains(@class, 'start view')]"), "Main Page")
        self.next_page_button = self._element_factory.get_button(Locator(By.XPATH, "//*[@class='start__link']"), "Next Page Button")

    def click_next_page_button(self):
        return self.next_page_button.click()

