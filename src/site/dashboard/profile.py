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
from src.site.dashboard.dashboard_locators import MyCloudText as mtxt
from src.site.template.template import Template


class Profile(User, Helper, Configuration, ToastMessage):
    def __init__(self, browser, read_credentials):
        super().__init__(read_credentials)
        self.cred = read_credentials
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def update_avatar(self):
        self.browser.find_element(*ploc.remove_button).click()
        time.sleep(1)
        self.browser.find_element(*ploc.input_image).send_keys((sys.path[1]) + '/utils/avatar.jpg')
        time.sleep(1)
        self.browser.find_element(*ploc.image_apply).click()
        time.sleep(1)
        self.browser.find_element(*ploc.image_remove).click()
        time.sleep(1)
        self.browser.find_element(*ploc.remove_button).click()

        self.browser.find_element(*ploc.input_image).send_keys((sys.path[1]) + '/utils/avatar.jpg')
        self.browser.find_element(*ploc.image_apply).click()

    def update_name(self, fname, lname):
        self.browser.find_element(*ploc.first_name).clear()
        self.browser.find_element(*ploc.first_name).send_keys(fname)
        self.browser.find_element(*ploc.last_name).clear()
        self.browser.find_element(*ploc.last_name).send_keys(lname)

    def change_personal_info(self, fname, lname):
        self.browser.refresh()
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.profile_info).click()
        # Update Avatar
        self.update_avatar()
        # Update Name
        self.update_name(fname, lname)
        # Save Changes
        self.browser.find_element(*ploc.update_button).click()
        self.check_toast_message('Your profile is updated successfully.')

    def update_email(self, email):
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.profile_info).click()
        self.browser.find_element(*ploc.email).clear()
        self.browser.find_element(*ploc.email).send_keys("thisisawrong@passowrd")
        self.browser.find_element(*ploc.update_button).click()
        time.sleep(1)
        self.check_toast_message("Please provide a valid email format.")
        time.sleep(1)
        self.browser.find_element(*ploc.email).clear()
        self.browser.find_element(*ploc.email).send_keys(email)
        self.browser.find_element(*ploc.update_button).click()

        self.check_toast_message("Your profile is updated successfully. To change email, verify your new email. "
                                 "Check inbox in " + email + " for instructions.")

        assert_that(self.browser.find_element(*ploc.email_update_notice).text). \
            is_equal_to("Your profile is updated successfully. To change email, verify your new email. "
                        "Check inbox in " + email + " for instructions.")

    def change_password_empty_input_given(self):
        # Empty field
        self.browser.find_element(*ploc.change_pass_button).click()
        self.check_toast_message("Enter your current password")
        time.sleep(1)
        # Empty New password & Confirm Password
        self.browser.find_element(*ploc.current_pass).send_keys("wrong password")
        self.browser.find_element(*ploc.change_pass_button).click()
        self.check_toast_message("At least 8 characters, uppercase, lowercase and number needed.")
        time.sleep(1)

    def change_password_wrong_password_given(self, password):
        self.browser.find_element(*ploc.current_pass).send_keys("wrong password")
        self.browser.find_element(*ploc.new_pass).send_keys(password)
        self.browser.find_element(*ploc.con_new_pass).send_keys(password)
        self.browser.find_element(*ploc.change_pass_button).click()
        self.check_toast_message("Current password doesn't match")
        time.sleep(1)

    def change_password_same_password_given(self):
        self.browser.find_element(*ploc.current_pass).click()
        self.browser.find_element(*ploc.current_pass).send_keys(self.get_password())
        self.browser.find_element(*ploc.new_pass).send_keys(self.get_password())
        self.browser.find_element(*ploc.con_new_pass).send_keys(self.get_password())
        self.browser.find_element(*ploc.change_pass_button).click()
        self.check_toast_message("Password must differ from old password")
        time.sleep(1)

    def change_password_password_not_matching(self, password):
        self.browser.find_element(*ploc.current_pass).send_keys(self.get_password())
        self.browser.find_element(*ploc.new_pass).send_keys(password)
        self.browser.find_element(*ploc.con_new_pass).send_keys(password + "foo")
        self.browser.find_element(*ploc.change_pass_button).click()
        self.check_toast_message("New password and confirmed password must match")
        time.sleep(1)

    def change_password_correct(self, user, password):
        self.browser.find_element(*ploc.current_pass).clear()
        self.browser.find_element(*ploc.current_pass).send_keys(self.get_password())
        self.browser.find_element(*ploc.new_pass).clear()
        self.browser.find_element(*ploc.new_pass).send_keys(password)
        self.browser.find_element(*ploc.con_new_pass).clear()
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

    def change_password(self, user, password):
        self.browser.refresh()
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.change_pass).click()
        # Empty field
        self.change_password_empty_input_given()
        # Wrong Password
        self.change_password_wrong_password_given(password)
        # Same Password
        self.change_password_same_password_given()
        # Confirm not matching
        self.change_password_password_not_matching(password)
        # All Correct
        self.change_password_correct(user, password)

    def payment_method(self, card):
        self.browser.refresh()
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.payment_method).click()
        self.browser.find_element(*ploc.add_card).click()
        time.sleep(1)
        if self.DEV:
            self.browser.find_element(*ploc.stripe_email).clear()
            self.browser.find_element(*ploc.stripe_email).send_keys(self.get_email())
            self.browser.find_element(*ploc.stripe_card_number).clear()
            self.browser.find_element(*ploc.stripe_card_number).send_keys(card)
            self.browser.find_element(*ploc.stripe_card_expiry_date).clear()
            self.browser.find_element(*ploc.stripe_card_expiry_date).send_keys("444")
            self.browser.find_element(*ploc.stripe_card_cvc_number).clear()
            self.browser.find_element(*ploc.stripe_card_cvc_number).send_keys("424")
            self.browser.find_element(*ploc.stripe_card_name).clear()
            self.browser.find_element(*ploc.stripe_card_name).send_keys("TesterBhai")
            self.browser.find_element(*ploc.save_card).click()
        else:
            self.browser.find_element(*ploc.back_to_dashboard).click()

        time.sleep(1)
        self.browser.find_element(*ploc.go_to_home).click()
        assert_that(self.browser.find_element(*dloc.title).text).is_equal_to(mtxt.title_text)

    def payment_method_remove_delete_card(self):
        if self.DEV:
            self.browser.find_element(*dloc.d_profile).click()
            self.browser.find_element(*ploc.payment_method).click()

            self.browser.find_element(*ploc.set_card_as_default).click()
            time.sleep(1)
            assert_that(self.browser.find_element(*ploc.set_new_card_as_default).text).\
                is_equal_to("Set as Default")
            time.sleep(1)
            self.browser.find_element(*ploc.delete_card_2).click()
            time.sleep(1)

            while len(self.browser.find_elements(*ploc.delete_card)) > 0:
                assert_that("Success").is_equal_to("Card is not being deleted")

    def my_favorites(self, price, category):
        self.browser.refresh()
        self.browser.find_element(*dloc.d_profile).click()
        self.browser.find_element(*ploc.payment_method).click()
        self.browser.find_element(*ploc.my_favorites).click()

        self.browser.find_element(*ploc.price_select).click()
        with soft_assertions():
            if price.__eq__("starter"):
                self.browser.find_element(*ploc.price_select_starter).click()
            elif price.__eq__("pro"):
                self.browser.find_element(*ploc.price_select_pro).click()
            else:
                self.browser.find_element(*ploc.price_select_all).click()

            self.browser.find_element(*ploc.category_select).click()
            if category.__eq__("block"):
                self.browser.find_element(*ploc.category_select_blocks).click()
            elif category.__eq__("page"):
                self.browser.find_element(*ploc.category_select_pages).click()
            elif category.__eq__("pack"):
                self.browser.find_element(*ploc.category_select_packs).click()
            else:
                self.browser.find_element(*ploc.category_select_all).click()

            WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located((By.XPATH, ploc.image_on_template)))

            assert_that(self.browser.find_element(*ploc.price_on_template).text).is_equal_to(price.upper())
            assert_that(self.browser.find_element(*ploc.category_on_template).text).is_equal_to(category.upper())

            temp_price = self.browser.find_element(*ploc.price_on_template).text
            temp_cat = self.browser.find_element(*ploc.category_on_template).text
            temp_rate = self.browser.find_element(*ploc.ratings_on_template).text
            temp_down = self.browser.find_element(*ploc.downloads_on_template).text
            title = self.browser.find_element(*ploc.title_on_template)
            temp_title = title.text
            self.cursor.move_to_element(title).click().perform()
            temp = Template(self.browser)
            temp.check_template(category, temp_title, temp_price, temp_cat, temp_rate, temp_down)




