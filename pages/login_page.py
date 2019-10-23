from .base_page import BasePage
from .locators import BasePageLocators, LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.driver.find_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.driver.find_element(*LoginPageLocators.PASSWORD_REGISTRATION_CONFIRM).send_keys(password)
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

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
