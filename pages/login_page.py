from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.driver.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_input.send_keys(email)
        password_input = self.driver.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_input.send_keys(password)
        password_confirm_input = self.driver.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_CONFIRM)
        password_confirm_input.send_keys(password)
        btn = self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON)
        btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is invalid'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
