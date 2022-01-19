import time

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains

from utils.helper import CheckText, CheckVisibility
from src.site.forgetpassword.forget_password_locators import ForgetPassLocators as loc
from src.site.forgetpassword.forget_password_locators import ForgetPassText as txt
from src.site.signin.signin_locators import SignInLocators as sloc
from src.site.signin.signin_locators import SignInText as stxt


class ForgetPassword:
    def __init__(self, browser):
        self.browser = browser
        self.c = CheckText(self.browser)
        self.d = CheckVisibility(self.browser)
        self.cursor = ActionChains(self.browser)

    def load(self):
        self.browser.get()

    def check_forget_password_on_page(self):
        self.browser.find_element(*sloc.forget_pass).click()
        time.sleep(1)
        self.d.check_visibility(loc.icon, "Icon is not visible")
        assert_that(self.browser.find_element(*loc.title).text).is_equal_to(txt.title_text)
        assert_that(self.browser.find_element(*loc.des).text).is_equal_to(txt.des)
        self.browser.find_element(*loc.sign_in_page).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*sloc.title).text).is_equal_to(stxt.sign_in_title_txt)

    def check_forget_password_on_modal(self):
        self.browser.find_element(*sloc.forget_pass).click()
        time.sleep(1)
        self.d.check_visibility(loc.modal_icon, "Icon is not visible")
        assert_that(self.browser.find_element(*loc.modal_title).text).is_equal_to(txt.modal_title_text)
        self.browser.find_element(*loc.sign_in_page).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*sloc.modal_title).text).is_equal_to(stxt.sign_in_title_txt)

    def forget_password_through_modal(self, email):
        self.browser.find_element(*loc.email_field).send_keys(email)
        self.browser.find_element(*loc.toast_close_btn).click()

        time.sleep(1.5)
        assert_that(self.browser.find_element(*loc.success_msg).text).is_equal_to(txt.success_msg_text)
        self.browser.find_element(*loc.toast_close_btn).click()
