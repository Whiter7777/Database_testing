from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from integration_template.utilities.password_generator import PasswordGenerator

class LoginForm(Form):
    
    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[@class='login-form']"), "Login Form")
        self.password_input = self._element_factory.get_text_box(Locator(By.XPATH, "//*[@placeholder='Choose Password']"), "Input Password")

    def enter_password(self):
        self.password_input.clear()
        self.password_input.type(PasswordGenerator().generate_password())