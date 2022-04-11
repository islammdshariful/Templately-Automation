import os

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains

from src.site.dashboard.my_workspace import MyWorkSpace
from utils.helper import ToastMessage, Helper
from src.site.dashboard.dashboard_locators import MyCloudLocators as cl
from src.site.dashboard.dashboard_locators import DashboardLocators as d
from src.site.dashboard.dashboard_locators import SearchTemplateLocators as sloc
from src.site.dashboard.dashboard_locators import TemplateLocators as tloc
from src.site.dashboard.dashboard_locators import MyCloudText as cltxt
import time


class MyCloud(Helper, ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)
        self.ws = MyWorkSpace(browser)

    def load(self, url):
        self.browser.get(url)

    def select_platform(self, platform):
        self.browser.find_element(*cl.select_platform).click()
        if platform.__eq__('elementor'):
            self.browser.find_element(*cl.platform_elementor).click()
        else:
            self.browser.find_element(*cl.platform_gutenberg).click()

    def download_template(self, platform):
        self.browser.find_element(*d.d_cloud).click()
        # Select platform
        self.select_platform(platform)
        # Template
        template_name = self.browser.find_element(*tloc.template_1_name).text
        # Open menu for Download
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)
        self.browser.find_element(*tloc.template_1_menu_download).click()
        file = self.file_path + 'Downloads\\' + template_name + '.json'

        time_to_wait = 10
        time_counter = 0
        while not os.path.exists(file):
            time.sleep(1)
            time_counter += 1
            if time_counter > time_to_wait:
                break

        if os.path.isfile(file):
            pass
        else:
            assert_that('Success').is_equal_to("%s isn't a file!" % file)
        # Close menu
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)

    def copy_to_workspace(self, platform):
        self.browser.find_element(*d.d_cloud).click()
        # Select platform
        self.select_platform(platform)
        # Template
        template_name = self.browser.find_element(*tloc.template_1_name).text
        # Open menu to Copy
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)
        self.browser.find_element(*tloc.template_1_menu_copy).click()
        time.sleep(1)
        self.browser.find_element(*tloc.copy_move_modal_select_ws).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_0).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_done).click()

        self.check_toast_message('File copied to WorkSpace successfully')

        # Check template inside workspace
        self.ws.check_template_inside_workspace(template_name)

    def move_to_workspace(self, platform):
        self.browser.find_element(*d.d_cloud).click()
        # Select platform
        self.select_platform(platform)
        # Template
        template_name = self.browser.find_element(*tloc.template_1_name).text
        # Move
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)
        self.browser.find_element(*tloc.template_1_menu_move).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_0).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_done).click()

        self.check_toast_message('File moved to WorkSpace successfully')

        # Check template inside workspace
        self.ws.check_template_inside_workspace(template_name)

    def delete_template(self, platform):
        self.browser.find_element(*d.d_cloud).click()
        # Select platform
        self.select_platform(platform)
        # Template name before deletion
        template_name_before_deletion = self.browser.find_element(*tloc.template_1_name).text
        # Delete
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)
        self.browser.find_element(*tloc.template_1_menu_delete).click()
        with soft_assertions():
            assert_that(self.browser.find_element(*tloc.delete_modal_title).text).is_equal_to("Are You Sure?")
            assert_that(self.browser.find_element(*tloc.delete_modal_des).text).\
                is_equal_to("The file will be deleted permanently")
        self.browser.find_element(*tloc.delete_modal_cancel_button).click()
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)
        self.browser.find_element(*tloc.template_1_menu_delete).click()
        self.browser.find_element(*tloc.delete_modal_delete_button).click()

        self.check_toast_message("My Cloud file deleted successfully.")

        # Template name after deletion
        template_name_after_deletion = self.browser.find_element(*tloc.template_1_name).text

        if template_name_before_deletion.__eq__(template_name_after_deletion):
            assert_that("Success").is_equal_to("Template deletion unsuccessful")

    def search_template(self, query):
        with soft_assertions():
            self.browser.find_element(*d.d_cloud).click()
            self.browser.find_element(*sloc.search_input).click()
            self.browser.find_element(*sloc.search_input).send_keys(cltxt.search_invalid_template)
            self.browser.find_element(*sloc.search_button).click()
            assert_that(self.browser.find_element(*sloc.search_result_empty).text).\
                is_equal_to(cltxt.search_template_not_found_message)
            self.browser.find_element(*sloc.search_close_button).click()
            self.browser.find_element(*sloc.search_input).click()
            self.browser.find_element(*sloc.search_input).send_keys(query)
            self.browser.find_element(*sloc.search_button).click()
            time.sleep(1)

            template_name = self.browser.find_element(*tloc.template_1_name).text

            assert_that(template_name).is_equal_to(query)

    def change_layout(self, layout):
        self.browser.find_element(*d.d_cloud).click()
        if layout.__eq__('grid'):
            self.browser.find_element(*cl.view_grid).click()
            time.sleep(1)
            if not len(self.browser.find_elements(*tloc.template_1_date)) > 0:
                assert_that("Success").is_equal_to("Layout " + layout + "Not changed.")
        else:
            self.browser.find_element(*cl.view_list).click()
            if not len(self.browser.find_elements(*tloc.template_1_date)) > 0:
                assert_that("Success").is_equal_to("Layout " + layout + "Not changed.")
