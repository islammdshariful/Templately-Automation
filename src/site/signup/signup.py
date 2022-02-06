import time

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.helper import Helper
from src.site.signup.signup_locators import SignUpLocators as loc
from src.site.signup.signup_locators import SignUpText as txt
from src.site.signin.signin_locators import SignInLocators as sloc
from src.site.signin.signin_locators import SignInText as stxt


class SignUp(Helper):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def go_to_signin_page(self):
        self.browser.find_element(*loc.signin_page).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*sloc.welcome_msg).text).is_equal_to(stxt.welcome_ms_txt)
        self.browser.find_element(*sloc.create_acc).click()
        time.sleep(1)

    def go_to_policy_page(self):
        self.browser.find_element(*loc.policy_page).click()
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, "//h4[normalize-space()='Privacy Policy']").text). \
            is_equal_to("Privacy Policy")
        self.browser.back()
        time.sleep(1)

    def go_to_terms_page(self):
        self.browser.find_element(*loc.terms_page).click()
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, "//h4[normalize-space()='Terms of Services']").text). \
            is_equal_to("Terms of Services")
        self.browser.back()
        time.sleep(1)

    def create_an_account(self, first_name, last_name, email, password, con_password):
        with soft_assertions():
            self.browser.find_element(*loc.fname_field).send_keys(first_name)
            self.browser.find_element(*loc.lname_field).send_keys(last_name)
            self.browser.find_element(*loc.email_field).send_keys(email)
            self.browser.find_element(*loc.pass_field).send_keys(password)
            self.browser.find_element(*loc.con_pass_field).send_keys(con_password)

            self.browser.find_element(*loc.policy_field).click()
            self.browser.find_element(*loc.terms_field).click()

            self.browser.find_element(*loc.signup_btn).click()

            assert_that(self.browser.find_element(*loc.success_msg).text).is_equal_to(txt.success_msg_text)
            time.sleep(1)
            self.browser.find_element(*loc.toast_close_btn).click()

    def check_signup_page(self):
        with soft_assertions():
            self.check_visibility(loc.icon, "Singup Page icon is not visible")
            self.check_visibility(loc.img, "Singup Page image is not visible")

            # Go to Signin Page
            self.go_to_signin_page()

            # Go to Policy Page
            self.go_to_policy_page()

            # Go to Terms Page
            self.go_to_terms_page()

            # Create a account
            # self.create_an_account()

