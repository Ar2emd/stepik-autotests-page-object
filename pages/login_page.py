from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absent"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absent"

    def register_new_user(self, email, password):
        register_form_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        register_form_email.send_keys(email)
        register_form_password1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD1)
        register_form_password1.send_keys(password)
        register_form_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
        register_form_password2.send_keys(password)
        register_submit_button = self.browser.find_element(*LoginPageLocators.REFISTER_SUBMIT_BUTTON)
        register_submit_button.click()
