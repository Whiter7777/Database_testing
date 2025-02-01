from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from pages.forms.login_form import LoginForm

class GamePage(Form):
    __login_form = LoginForm()

    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[contains(@class, 'game view')]"), "Game Page")

    @property
    def login_form(self):
        return self.__login_form
