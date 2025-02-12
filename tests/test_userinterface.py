import allure
from tests.test_base import TestBase
from pages.main_page import MainPage
from pages.game_page import GamePage
from integration_template.utilities.get_random_data import GetRandomData
from integration_template.utilities.upload_file_to_explorer import UploadFile
from integration_template.configurations.testing_data_configuration import TestDataConfiguration


class TestUserInterface(TestBase):
    main_page = MainPage()
    game_page = GamePage()

    def setup_method(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

    def test_fill_in_the_forms(self):
        with allure.step("Main page is displayed"):
            assert self.main_page.is_page_displayed()

        with allure.step("Click Next Page Button"):
            self.main_page.click_next_page_button()

        with allure.step("Game page is displayed"):
            assert self.game_page.is_page_displayed()

        with allure.step("Login form is displayed"):
            assert self.game_page.login_form.is_page_displayed()

        email = GetRandomData().generate_random_text(
            TestDataConfiguration().get_test_data().email_letters_quant_in_range)

        with allure.step("Enter password"):
            self.game_page.login_form.enter_password(
                GetRandomData().generate_password(
                    TestDataConfiguration().get_test_data().lat_letters_quant_in_range,
                    TestDataConfiguration().get_test_data().cyr_letters_quant_in_range,
                    TestDataConfiguration().get_test_data().digit_quant_in_range)+email
            )

        with allure.step("Enter email"):
            self.game_page.login_form.enter_email(email)

        with allure.step("Enter domain"):
            self.game_page.login_form.enter_domain(
                GetRandomData().generate_random_text(
                    TestDataConfiguration().get_test_data().domain_letters_quant_in_range)
            )

        with allure.step("Check dropdown"):
            self.game_page.login_form.check_dropdown_list()

        with allure.step("Check accept"):
            self.game_page.login_form.check_accept()

        with allure.step("Click next button"):
            self.game_page.login_form.click_next_button()

        with allure.step("Avatar form is displayed"):
            assert self.game_page.avatar_form.is_page_displayed()

        with allure.step("Attach file"):
            self.game_page.avatar_form.attach_file()
            UploadFile().upload_file_to_explorer()

        with allure.step("Check random interests"):
            self.game_page.avatar_form.check_random_checkboxes(
                TestDataConfiguration().get_test_data().number_selected_checkboxes)

        with allure.step("Click next button"):
            self.game_page.avatar_form.click_next_button()

        with allure.step("Personal Details Form id displayed"):
            self.game_page.personal_details_form.is_page_displayed()

    def test_hide_help_form(self):
        self.setup_method()

        with allure.step("Main page is displayed"):
            assert self.main_page.is_page_displayed()

        with allure.step("Click Next Page Button"):
            self.main_page.click_next_page_button()

        with allure.step("Game page is displayed"):
            assert self.game_page.is_page_displayed()

        with allure.step("Help form is displayed"):
            assert self.game_page.help_form.is_page_displayed()

        with allure.step("Click Send to Bottom Button"):
            self.game_page.help_form.click_send_to_bottom_button()

        with allure.step("Help Form is hidden"):
            assert self.game_page.help_form.is_help_form_hidden()

    def test_accept_cookies(self):
        self.setup_method()

        with allure.step("Main page is displayed"):
            assert self.main_page.is_page_displayed()

        with allure.step("Click Next Page Button"):
            self.main_page.click_next_page_button()

        with allure.step("Game page is displayed"):
            assert self.game_page.is_page_displayed()

        with allure.step("Cookies form is displayed"):
            assert self.game_page.cookies_form.is_page_displayed()

        with allure.step("Accept Cookies"):
            self.game_page.cookies_form.accept_cookies()

        with allure.step("Cookies form is not displayed"):
            assert self.game_page.cookies_form.is_page_not_displayed()

    def test_timer_start_value(self):
        self.setup_method()

        with allure.step("Main page is displayed"):
            assert self.main_page.is_page_displayed()

        with allure.step("Click Next Page Button"):
            self.main_page.click_next_page_button()

        with allure.step("Game page is displayed"):
            assert self.game_page.is_page_displayed()

        with allure.step("Timer is 00:00:00"):
            assert self.game_page.check_timer(
                TestDataConfiguration().get_test_data().timer_start_value
            )
