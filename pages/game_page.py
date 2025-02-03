from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from pages.forms.login_form import LoginForm
from pages.forms.avatar_form import AvatarForm
from pages.forms.cookies_form import CookiesForm
from pages.forms.help_form import HelpForm
from pages.forms.personal_details_form import PersonalDetailsForm
from integration_template.configurations.test_data_configuration import TestDataConfiguration


class GamePage(Form):
    __login_form = LoginForm()
    __avatar_form = AvatarForm()
    __cookies_form = CookiesForm()
    __help_form = HelpForm()
    __personal_details_form = PersonalDetailsForm()

    def __init__(self):
        super().__init__(Locator(By.XPATH, "//*[contains(@class, 'game view')]"), "Game Page")
        self.timer = self._element_factory.get_text_box(
            Locator(By.XPATH, "//*[@class='timer timer--white timer--center']"),
            "Timer")

    @property
    def login_form(self):
        return self.__login_form

    @property
    def avatar_form(self):
        return self.__avatar_form

    @property
    def cookies_form(self):
        return self.__cookies_form

    @property
    def help_form(self):
        return self.__help_form

    @property
    def personal_details_form(self):
        return self.__personal_details_form

    def page_is_displayed(self):
        return self.state.is_displayed()

    def check_timer(self):
        return self.timer.text == TestDataConfiguration().get_timer()
