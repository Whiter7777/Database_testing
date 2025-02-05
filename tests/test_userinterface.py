import allure
from tests.test_base import TestBase
from pages.main_page import MainPage
from pages.game_page import GamePage

class TestUserInterface(TestBase):
    main_page = MainPage()
    game_page = GamePage()

    def setup_method(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

        with allure.step("Main page is displayed"):
            assert self.main_page.page_is_displayed()

        with allure.step("Click Next Page Button"):
            self.main_page.click_next_page_button()

        with allure.step("Game page is displayed"):
            assert self.game_page.page_is_displayed()

    def test_userinterface(self):
        with allure.step("Login form is displayed"):
            assert self.game_page.login_form.page_is_displayed()

        with allure.step("Enter user data"):
            self.game_page.login_form.enter_user_data()

        with allure.step("Check accept"):
            self.game_page.login_form.check_accept()

        with allure.step("Click next button"):
            self.game_page.login_form.click_next_button()

        with allure.step("Avatar form is displayed"):
            assert self.game_page.avatar_form.page_is_displayed()

        with allure.step("Attach file"):
            self.game_page.avatar_form.attach_file()

        with allure.step("Check random interests"):
            self.game_page.avatar_form.check_random_checkboxes()

        with allure.step("Click next button"):
            self.game_page.avatar_form.click_next_button()

        with allure.step("Personal Details Form id displayed"):
            self.game_page.personal_details_form.page_is_displayed()

    def test_help_form(self):
        self.setup_method()

        with allure.step("Help form is displayed"):
            assert self.game_page.help_form.page_is_displayed()

        with allure.step("Click Send to Bottom Button"):
            self.game_page.help_form.click_send_to_bottom_button()

        with allure.step("Help Form is hidden"):
            assert self.game_page.help_form.help_form_is_hidden()

    def test_cookies(self):
        self.setup_method()

        with allure.step("Cookies form is displayed"):
            assert self.game_page.cookies_form.page_is_displayed()

        with allure.step("Accept Cookies"):
            self.game_page.cookies_form.accept_cookies()

        with allure.step("Cookies form is not displayed"):
            assert self.game_page.cookies_form.page_is_not_displayed()

    def test_timer(self):
        self.setup_method()

        with allure.step("Timer is 00:00:00"):
            assert self.game_page.check_timer()

