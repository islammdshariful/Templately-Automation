from datetime import datetime

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.helper import Helper, ToastMessage
from src.site.dashboard.dashboard_locators import DashboardLocators as dloc
from src.site.dashboard.dashboard_locators import ManageAPIsLocators as mloc


class ManageAPI(Helper, ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def check_create_token_validation(self, token_name):
        self.browser.find_element(*mloc.terms_of_services).click()
        self.browser.find_element(*mloc.create_token).click()
        self.check_toast_message("Only numbers, letters and spaces are permitted in token name")
        self.browser.find_element(*mloc.token_name).clear()
        self.browser.find_element(*mloc.token_name).send_keys(token_name)

        self.browser.find_element(*mloc.terms_of_services).click()
        self.browser.find_element(*mloc.create_token).click()
        self.check_toast_message("Please agree to Terms of Services.")

    def check_token_modal(self):
        self.check_visibility(mloc.token_label, "Token label is not visible")
        self.check_visibility(mloc.registered_token, "Registered token is not showing")
        token = self.browser.find_element(By.XPATH, mloc.registered_token).text

        self.browser.find_element(*mloc.copy_token).click()
        self.browser.find_element(*mloc.token_copied_condition).click()
        self.check_toast_message("Copied")
        self.browser.find_element(*mloc.wahoo_got_it_btn).click()

        return token

    def create_token(self):
        with soft_assertions():
            self.browser.find_element(*dloc.d_api).click()
            now = datetime.now()
            token_name = now.strftime("%H-%M-%S")

            self.browser.find_element(*mloc.token_name).send_keys(token_name)
            token_name = now.strftime("Token " + "%H %M %S")
            self.check_create_token_validation(token_name)
            self.browser.find_element(*mloc.terms_of_services).click()
            self.browser.find_element(*mloc.create_token).click()

            token = self.check_token_modal()

            assert_that(self.browser.find_element(*mloc.token_1_name).text).is_equal_to(token_name)
            assert_that(self.browser.find_element(*mloc.token_1_api_key).text).is_equal_to(token)
            assert_that(self.browser.find_element(*mloc.token_1_active_sites).text).\
                is_equal_to("Currently not being used in any site.")

    def copy_token(self):
        self.browser.find_element(*mloc.token_1_copy).click()
        self.check_toast_message("Copied")

    def delete_token(self):
        self.browser.find_element(*mloc.token_1_delete).click()
        self.browser.find_element(*mloc.delete_modal_cancel).click()
        self.browser.find_element(*mloc.token_1_delete).click()
        self.browser.find_element(*mloc.delete_modal_delete).click()
        self.check_toast_message("API key deleted successfully.")



