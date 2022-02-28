import time

from assertpy import assert_that
from selenium.webdriver import ActionChains, Keys

from utils.helper import Helper, ToastMessage
from utils.configuration import Configuration
from src.site.checkout.checkout_locators import CheckoutLocators as cloc
from src.site.dashboard.dashboard_locators import SubscriptionLocators as sloc
from src.site.home.home_page_locators import HomePageTexts as htxt


class Checkout(ToastMessage, Configuration):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def check_items_price(self, package, type):
        # Package name & prices
        # Total Label
        assert_that(self.browser.find_element(*cloc.total_label).text).is_equal_to("Total")
        if package.__eq__('premium') and type.__eq__('monthly'):
            assert_that(self.browser.find_element(*cloc.item_name).text).is_equal_to(package.capitalize() + " " + type)
            assert_that(self.browser.find_element(*cloc.item_price).text).is_equal_to(htxt.mon_prem_price_txt)
            # Total Price
            assert_that(self.browser.find_element(*cloc.total_ammount).text).is_equal_to(htxt.mon_prem_disc_price_txt)

        elif package.__eq__('premium') and type.__eq__('yearly'):
            assert_that(self.browser.find_element(*cloc.item_name).text).is_equal_to(package.capitalize() + " " + type)
            assert_that(self.browser.find_element(*cloc.item_price).text).is_equal_to(htxt.ann_prem_price_txt)
            # Total Price
            assert_that(self.browser.find_element(*cloc.total_ammount).text).is_equal_to(htxt.ann_prem_disc_price_txt)
        else:
            assert_that(self.browser.find_element(*cloc.item_name).text).is_equal_to(package.capitalize())
            assert_that(self.browser.find_element(*cloc.item_price).text).is_equal_to(htxt.lftm_price_txt)
            # Total Price
            assert_that(self.browser.find_element(*cloc.total_ammount).text).is_equal_to(htxt.lftm_disc_price_txt)

    def check_discount(self, package, type):
        # Discount Name & Discount Percentages
        if package.__eq__('premium') and type.__eq__('monthly'):
            assert_that(self.browser.find_element(*cloc.discount_label).text).is_equal_to(htxt.mon_prem_discount_label)
            assert_that(self.browser.find_element(*cloc.discount_percentage).text).\
                is_equal_to(htxt.mon_prem_discount_percentage)
        elif package.__eq__('premium') and type.__eq__('yearly'):
            assert_that(self.browser.find_element(*cloc.discount_label).text).is_equal_to(htxt.ann_prem_discount_label)
            assert_that(self.browser.find_element(*cloc.discount_percentage).text).\
                is_equal_to(htxt.ann_prem_discount_percentage)
        else:
            assert_that(self.browser.find_element(*cloc.discount_label).text).is_equal_to(htxt.lftm_prem_discount_label)
            assert_that(self.browser.find_element(*cloc.discount_percentage).text).\
                is_equal_to(htxt.lftm_prem_discount_percentage)

    def check_coupon_validation(self, package, type):
        self.browser.find_element(*cloc.coupon_code_input).click()
        self.browser.find_element(*cloc.coupon_code_input).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*cloc.coupon_code_input).send_keys(Keys.CONTROL, 'c')
        self.browser.find_element(*cloc.coupon_code_input).click()

        self.browser.find_element(*cloc.coupon_code_input).send_keys("%")
        coupon_code = self.browser.find_element(*cloc.coupon_code_input).get_attribute('value')
        self.browser.find_element(*cloc.coupon_code_apply_btn).click()
        self.check_toast_message("No such coupon: '" + coupon_code + "'")
        if len(self.browser.find_elements(*cloc.discount_label)) > 0:
            assert_that("Success").is_equal_to("Discount name is still showing which should be hidden.")
        self.browser.find_element(*cloc.coupon_code_input).click()
        self.browser.find_element(*cloc.coupon_code_input).send_keys(Keys.CONTROL, 'a')
        self.browser.find_element(*cloc.coupon_code_input).send_keys(Keys.BACKSPACE)
        self.browser.find_element(*cloc.coupon_code_input).send_keys(Keys.CONTROL, 'v')
        self.browser.find_element(*cloc.coupon_code_apply_btn).click()
        # Discount Name & Discount Percentages
        self.check_discount(package, type)

    def check_checkout_information(self, package, type):
        # Package name & prices
        self.check_items_price(package, type)
        # Discount Name & Discount Percentages
        self.check_discount(package, type)
        # Check validation of coupon field
        self.check_coupon_validation(package, type)

    def pay_with_method(self, method):
        if method.__eq__("default"):
            self.browser.find_element(*cloc.pay_with_other_option).click()
            assert_that(self.browser.find_element(*cloc.choose_a_card_label).text).is_equal_to("Choose a Card")
            time.sleep(1)
            self.browser.find_element(*cloc.pay_with_default_method).click()
        else:
            self.browser.find_element(*cloc.pay_with_default_method).click()
            time.sleep(1)
            self.browser.find_element(*cloc.pay_with_other_option).click()
            assert_that(self.browser.find_element(*cloc.choose_a_card_label).text).is_equal_to("Choose a Card")
            if self.DEV:
                self.browser.find_element(*cloc.choose_card).click()

        self.browser.find_element(*cloc.terms_of_service).click()
        self.browser.find_element(*cloc.get_free_tips).click()
        self.browser.find_element(*cloc.pay_now_btn).click()
        time.sleep(1)
        if self.DEV:
            assert_that(self.browser.find_element(*sloc.plan_change_notice).text).\
                is_equal_to("You have successfully changed plan")
        else:
            self.browser.find_element(*cloc.back_to_home).click()



