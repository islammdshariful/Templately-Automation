import json
import sys
import time

from assertpy import assert_that, soft_assertions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helper import Helper, ToastMessage
from utils.configuration import Configuration
from utils.set_users import User
from src.site.dashboard.dashboard_locators import DashboardLocators as dloc
from src.site.dashboard.dashboard_locators import ProfileLocators as ploc


class Profile(User, Helper, Configuration, ToastMessage):
    def __init__(self, browser, read_credentials):
        super().__init__(read_credentials)
        self.cred = read_credentials
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def change_personal_info(self, fname, lname):
        self.browser.refresh()
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.profile_info).click()
        self.browser.find_element(*ploc.input_image). \
            send_keys(f"C:\\Users\\shari\\OneDrive\\Desktop\\for work\\img\\profile pictures\\man-profile.jpg")
        self.browser.find_element(*ploc.image_apply).click()
        self.browser.find_element(*ploc.image_remove).click()

        self.browser.find_element(*ploc.input_image). \
            send_keys(f"C:\\Users\\shari\\OneDrive\\Desktop\\for work\\img\\profile pictures\\man-profile.jpg")
        self.browser.find_element(*ploc.image_apply).click()

        self.browser.find_element(*ploc.first_name).clear()
        self.browser.find_element(*ploc.first_name).send_keys(fname)
        self.browser.find_element(*ploc.last_name).clear()
        self.browser.find_element(*ploc.last_name).send_keys(lname)
        self.browser.find_element(*ploc.update_button).click()

        self.check_toast_message('Your profile is updated successfully.')

    def update_email(self, email):
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.profile_info).click()
        self.browser.find_element(*ploc.email).clear()
        self.browser.find_element(*ploc.email).send_keys(email)
        self.browser.find_element(*ploc.update_button).click()

        self.check_toast_message("Your profile is updated successfully. To change email, verify your new email. "
                                 "Check inbox in " + email + " for instructions.")

        assert_that(self.browser.find_element(*ploc.email_update_notice).text). \
            is_equal_to("Your profile is updated successfully. To change email, verify your new email. "
                        "Check inbox in " + email + " for instructions.")

    def change_password(self, user, password):
        self.browser.refresh()
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.change_pass).click()

        self.browser.find_element(*ploc.current_pass).send_keys(self.get_password())
        self.browser.find_element(*ploc.new_pass).send_keys(password)
        self.browser.find_element(*ploc.con_new_pass).send_keys(password)
        self.browser.find_element(*ploc.change_pass_button).click()

        try:
            WebDriverWait(self.browser, 3).until(
                EC.text_to_be_present_in_element((By.XPATH, "//div[@role='alert']"),
                                                 'Password changed successfully.'))
            self.cred[user]["password"] = password
            with open(str(sys.path[1]) + '/utils/credentials.json', "w") as file:
                json.dump(self.cred, file, indent=4, sort_keys=True)

            self.check_toast_message("Password changed successfully.")
        except TimeoutException:
            with soft_assertions():
                assert_that("success").is_equal_to("Password Not Changed.")
                self.browser.find_element(By.XPATH, f"//button[@aria-label='close']//*[name()='svg']").click()
