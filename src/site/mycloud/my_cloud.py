from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from utils.helper import ToastMessage
from src.site.mycloud.my_cloud_locators import MyCloudLocators as loc
from src.site.home.home_page_locators import HomePageLocators as hloc
from src.site.home.home_page_locators import HomePageTexts as htxt
from datetime import date, datetime
import time


class MyCloudDashboard(ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def signout(self):
        self.browser.find_element(*hloc.my_cloud_btn).click()
        self.browser.find_element(*loc.p_menu).click()
        self.browser.find_element(*loc.p_menu_signout).click()
        assert_that(self.browser.find_element(*hloc.header).text).is_equal_to(htxt.header_txt)

    def create_workspace(self):
        self.browser.find_element(*loc.d_workspace).click()
        self.browser.find_element(*loc.ws_add).click()
        today = date.today()
        now = datetime.now()
        day = today.strftime("%d-%m-%Y-")
        tm = now.strftime("%H-%M-%S")
        name = day + tm
        self.browser.find_element(*loc.ws_name).clear()
        self.browser.find_element(*loc.ws_name).send_keys("WS " + name)
        self.browser.find_element(*loc.ws_email).clear()
        self.browser.find_element(*loc.ws_email).send_keys("testerbhaai@gmail.com")
        self.browser.find_element(*loc.ws_email_add).click()
        self.browser.find_element(*loc.ws_email_remove).click()
        self.browser.find_element(*loc.ws_email).send_keys("testerbhaai@gmail.com")
        self.browser.find_element(*loc.ws_create_ws).click()
        time.sleep(2)
        self.check_toast_message("WorkSpace created successfully")

        assert_that(self.browser.find_element(*loc.ws_title).text).is_equal_to("WS " + name)

    def edit_workspace(self):
        self.browser.find_element(*loc.ws_menu).click()
        self.browser.find_element(*loc.ws_menu_edit).click()
        today = date.today()
        now = datetime.now()
        day = today.strftime("%d-%m-%Y-")
        tm = now.strftime("%H-%M-%S")
        name = day + tm
        self.browser.find_element(*loc.ws_name).clear()
        self.browser.find_element(*loc.ws_name).send_keys("WS " + name)
        self.browser.find_element(*loc.ws_save).click()
        time.sleep(2)
        self.check_toast_message("WorkSpace updated successfully.")
        assert_that(self.browser.find_element(*loc.ws_title).text).is_equal_to("WS " + name)

    def delete_workspace(self, delete_files):
        self.browser.find_element(*loc.ws_menu).click()
        self.browser.find_element(*loc.ws_menu_delete).click()
        self.browser.find_element(*loc.ws_delete_cancel).click()

        self.browser.find_element(*loc.ws_menu).click()
        self.browser.find_element(*loc.ws_menu_delete).click()

        if delete_files.__eq__('yes'):
            self.browser.find_element(*loc.ws_delete_ws_files).click()

        self.browser.find_element(*loc.ws_delete).click()
        time.sleep(2)
        self.check_toast_message("WorkSpace deleted successfully.")


