import json
import sys
import time
import datetime
from datetime import datetime

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
from src.site.dashboard.dashboard_locators import SubscriptionLocators as sloc
from src.site.home.home_page_locators import HomePageTexts as htxt


class Subscription(Helper, ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def check_starter_package(self):
        self.check_visibility(sloc.monthly_pack_starter_icon, "Starter Icon is not visible.")
        assert_that(self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_title).text).\
            is_equal_to(htxt.mon_sta_label_txt)
        assert_that(self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_price).text).\
            is_equal_to(htxt.mon_sta_price_txt + htxt.mon_sta_disc_price_txt)
        # Template count
        self.check_visibility(sloc.monthly_pack_starter_des, "Starter Description is not visible.")
        items_count = self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des_temp_count).text
        item = items_count.split()
        if int(item[0]) < 1:
            assert_that("Success").is_equal_to("Starter Template count is wrong")
        # Description
        if self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des_item_1_title).is_displayed():
            assert_that("Success").is_equal_to("Starter items is auto expand which isn't right.")
            self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des).click()
        self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des).click()
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des_item_1_title).text). \
            is_equal_to(htxt.mon_sta_list_1_txt)
        assert_that(self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des_item_2_title).text). \
            is_equal_to(htxt.mon_sta_list_2_txt)
        assert_that(self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des_item_3_title).text). \
            is_equal_to(htxt.mon_sta_list_3_txt)
        self.check_visibility(sloc.monthly_pack_starter_des_item_1_icon, "Starter Items icon 1 is not visible.")
        self.check_visibility(sloc.monthly_pack_starter_des_item_2_icon, "Starter Items icon 2 is not visible.")
        self.check_visibility(sloc.monthly_pack_starter_des_item_3_icon, "Starter Items icon 3 is not visible.")
        self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des).click()
        time.sleep(1)
        if self.browser.find_element(By.XPATH, sloc.monthly_pack_starter_des_item_1_title).is_displayed():
            assert_that("Success").is_equal_to("Starter items in not collapsing")

    def check_premium_package(self):
        self.check_visibility(sloc.premium_pack_starter_icon, "Premium Icon is not visible.")
        assert_that(self.browser.find_element(By.XPATH, sloc.premium_pack_starter_title).text).\
            is_equal_to(htxt.mon_prem_label_txt)
        assert_that(self.browser.find_element(By.XPATH, sloc.premium_pack_starter_price).text).\
            is_equal_to(htxt.mon_prem_price_txt + htxt.mon_prem_disc_price_txt)
        # Template count
        self.check_visibility(sloc.monthly_pack_starter_des, "Premium Description is not visible.")
        items_count = self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des_temp_count).text
        item = items_count.split()
        if int(item[0]) < 1:
            assert_that("Success").is_equal_to("Premium Template count is wrong")
        # Description
        if self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des_item_1_title).is_displayed():
            assert_that("Success").is_equal_to("Premium items is auto expand which isn't right.")
            self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des).click()
        self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des).click()
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des_item_1_title).text). \
            is_equal_to(htxt.mon_prem_list_1_txt)
        assert_that(self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des_item_2_title).text). \
            is_equal_to(htxt.mon_prem_list_2_txt)
        self.check_visibility(sloc.premium_pack_starter_des_item_1_icon, "Premium Items icon 1 is not visible.")
        self.check_visibility(sloc.premium_pack_starter_des_item_2_icon, "Premium Items icon 2 is not visible.")
        self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des).click()
        time.sleep(1)
        if self.browser.find_element(By.XPATH, sloc.premium_pack_starter_des_item_1_title).is_displayed():
            assert_that("Success").is_equal_to("Premium items in not collapsing")

    def check_lifetime_package(self):
        self.browser.execute_script("window.scrollTo(0, 645)")
        time.sleep(1)
        self.check_visibility(sloc.lifetime_pack_starter_icon, "Lifetime Icon is not visible.")
        assert_that(self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_title).text).\
            is_equal_to(htxt.lftm_label_txt)
        assert_that(self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_price).text).\
            is_equal_to(htxt.lftm_price_txt + htxt.lftm_disc_price_txt)
        # Template count
        self.check_visibility(sloc.lifetime_pack_starter_des, "Lifetime Description is not visible.")
        items_count = self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des_temp_count).text
        item = items_count.split()
        if int(item[0]) < 1:
            assert_that("Success").is_equal_to("Lifetime Template count is wrong")
        # Description
        if self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des_item_1_title).is_displayed():
            assert_that("Success").is_equal_to("Lifetime items is auto expand which isn't right.")
            self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des).click()
        self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des).click()
        time.sleep(1)
        assert_that(self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des_item_1_title).text). \
            is_equal_to(htxt.mon_prem_list_1_txt)
        assert_that(self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des_item_2_title).text). \
            is_equal_to(htxt.mon_prem_list_2_txt)
        self.check_visibility(sloc.lifetime_pack_starter_des_item_1_icon, "Lifetime Items icon 1 is not visible.")
        self.check_visibility(sloc.lifetime_pack_starter_des_item_2_icon, "Lifetime Items icon 2 is not visible.")
        self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des).click()
        time.sleep(1)
        if self.browser.find_element(By.XPATH, sloc.lifetime_pack_starter_des_item_1_title).is_displayed():
            assert_that("Success").is_equal_to("Lifetime items in not collapsing")

    def check_subscription(self, pack):
        with soft_assertions():
            self.browser.find_element(*dloc.d_subscription).click()
            if pack.__eq__("monthly"):
                self.browser.find_element(*sloc.toggle_monthly).click()
                time.sleep(1)
                self.check_starter_package()
                self.check_premium_package()
                self.check_lifetime_package()
            else:
                pass

