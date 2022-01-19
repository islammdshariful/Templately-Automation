from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains

from src.site.forgetpassword.forget_password import ForgetPassword
from utils.helper import CheckText, CheckVisibility
from src.site.signin.signin_locators import SignInLocators as loc
from src.site.signin.signin_locators import SignInText as txt
from src.site.mycloud.my_cloud_locators import MyCloudLocators as mloc
from src.site.mycloud.my_cloud_locators import MyCloudText as mtxt
from utils.set_users import User


class SignIn(User):

    def __init__(self, browser, config):
        super().__init__(config)
        self.browser = browser
        self.c = CheckText(self.browser)
        self.d = CheckVisibility(self.browser)
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def login_through_modal(self):
        self.d.check_visibility(loc.modal_icon, "Icon is not visible.")
        assert_that(self.browser.find_element(*loc.modal_title).text).is_equal_to(txt.sign_in_title_txt)
        assert_that(self.browser.find_element(*loc.modal_welcome_msg).text).is_equal_to(txt.welcome_ms_txt)

        assert_that(self.browser.find_element(*loc.new_here_label).text).is_equal_to(txt.new_here_label_txt)
        assert_that(self.browser.find_element(*loc.forget_pass).text).is_equal_to(txt.forget_pass_txt)

        fp = ForgetPassword(self.browser)
        fp.check_forget_password_on_modal()

        self.browser.find_element(*loc.email_field).send_keys(self.get_email())
        self.browser.find_element(*loc.password_field).send_keys(self.get_password())

        self.browser.find_element(*loc.sing_in_btn).click()

        assert_that(self.browser.find_element(*mloc.title).text).is_equal_to(mtxt.title_text)

    def login_through_page(self):
        self.d.check_visibility(loc.icon, "Icon is not visible.")
        assert_that(self.browser.find_element(*loc.title).text).is_equal_to(txt.sign_in_title_txt)
        assert_that(self.browser.find_element(*loc.welcome_msg).text).is_equal_to(txt.welcome_ms_txt)

        assert_that(self.browser.find_element(*loc.new_here_label).text).is_equal_to(txt.new_here_label_txt)
        assert_that(self.browser.find_element(*loc.forget_pass).text).is_equal_to(txt.forget_pass_txt)

        fp = ForgetPassword(self.browser)
        fp.check_forget_password_on_page()

        self.browser.find_element(*loc.email_field).send_keys(self.get_email())
        self.browser.find_element(*loc.password_field).send_keys(self.get_password())

        self.browser.find_element(*loc.sing_in_btn).click()

        assert_that(self.browser.find_element(*mloc.title).text).is_equal_to(mtxt.title_text)

    def testcase(self):
        with soft_assertions():
            # Login through Modal
            self.login_through_page()

