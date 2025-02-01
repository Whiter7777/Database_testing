import allure
from tests.test_base import TestBase
from pages.main_page import MainPage
from pages.game_page import GamePage
import time
class TestUserInterface(TestBase):
    main_page = MainPage()
    game_page = GamePage()

    def setup(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

        with allure.step("Main page is displayed"):
            assert self.main_page.state.is_displayed()

    def test_userinterface(self):
        with allure.step("Check Next Page Button"):
            assert self.main_page.next_page_button.state.is_displayed()

        with allure.step("Click Next Page Button"):
            self.main_page.click_next_page_button()

        with allure.step("Game page is displayed"):
            assert self.game_page.state.is_displayed()

        with allure.step("Login form is displayed"):
            assert self.game_page.login_form.state.is_displayed()

        with allure.step("Enter your password"):
            self.game_page.login_form.enter_password()

