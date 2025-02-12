from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.common.by import By
from py_selenium_auto.elements.button import Button
import random


class LoginForm(Form):

    def __init__(self):
        super().__init__(Locator(By.CLASS_NAME, "login-form"), "Login Form")
        self.password_input = self._element_factory.get_text_box(
            Locator(By.XPATH, "//*[@placeholder='Choose Password']"),
            "Input Password")
        self.email_input = self._element_factory.get_text_box(
            Locator(By.XPATH, "//*[@placeholder='Your email']"),
            "Input Email")
        self.domain_input = self._element_factory.get_text_box(
            Locator(By.XPATH, "//*[@placeholder='Domain']"),
            "Input Domain")
        self.dropdown_opener = self._element_factory.get_button(
            Locator(By.CLASS_NAME, "dropdown__opener"),
            "Dropdown Opener")
        self.accept_check_box = self._element_factory.get_check_box(
            Locator(By.CLASS_NAME, "checkbox__box"),
            "Accept Check Box")
        self.next_button = self._element_factory.get_button(
            Locator(By.CLASS_NAME, "button--secondary"),
            "Next Button")

    def is_page_displayed(self):
        return self.state.is_displayed()

    def enter_password(self, password: str):
        self.password_input.clear_and_type(password)

    def enter_email(self, email: str):
        self.email_input.clear_and_type(email)

    def enter_domain(self, domain: str):
        self.domain_input.clear_and_type(domain)

    def check_dropdown_list(self):
        self.dropdown_opener.click()
        dropdown_list = self._element_factory.find_elements(
            Button,
            Locator(By.CLASS_NAME, "dropdown__list-item"),
            "Dropdown List")
        random.choice(dropdown_list).click()

    def check_accept(self):
        if self.accept_check_box.check():
            self.accept_check_box.click()

    def click_next_button(self):
        if self.next_button.state.is_enabled():
            self.next_button.click()
