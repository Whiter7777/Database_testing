from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By


class PersonalDetailsForm(Form):
    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[@class='personal-details__form']"), "Personal Details Form")

    def page_is_displayed(self):
        return self.state.is_displayed()
