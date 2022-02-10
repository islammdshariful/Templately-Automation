import os

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from utils.helper import ToastMessage, Helper
from src.site.mycloud.my_cloud_locators import MyWorkSpaceLocators as ws
from src.site.mycloud.my_cloud_locators import MyCloudLocators as cl
from src.site.mycloud.my_cloud_locators import DashboardLocators as d
from src.site.mycloud.my_cloud_locators import SearchTemplateLocators as sloc
from src.site.mycloud.my_cloud_locators import TemplateLocators as tloc
from src.site.mycloud.my_cloud_locators import MyCloudText as cltxt
from src.site.home.home_page_locators import HomePageLocators as hloc
from src.site.home.home_page_locators import HomePageTexts as htxt
from datetime import date, datetime
import time


class Dashboard:
    def __init__(self, browser):
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def sign_out(self):
        self.browser.find_element(*hloc.my_cloud_btn).click()
        self.browser.find_element(*d.p_menu).click()
        self.browser.find_element(*d.p_menu_signout).click()
        assert_that(self.browser.find_element(*hloc.header).text).is_equal_to(htxt.header_txt)


class MyWorkSpace(ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def create_workspace(self, add_people_email):
        self.browser.find_element(*d.d_workspace).click()
        self.browser.find_element(*ws.ws_add).click()
        today = date.today()
        now = datetime.now()
        day = today.strftime("%d-%m-%Y-")
        tm = now.strftime("%H-%M-%S")
        name = day + tm
        self.browser.find_element(*ws.ws_name).clear()
        self.browser.find_element(*ws.ws_name).send_keys("WS " + name)
        self.browser.find_element(*ws.ws_email).clear()
        self.browser.find_element(*ws.ws_email).send_keys(add_people_email)
        self.browser.find_element(*ws.ws_email_add).click()
        self.browser.find_element(*ws.ws_email_remove).click()
        self.browser.find_element(*ws.ws_email).send_keys(add_people_email)
        self.browser.find_element(*ws.ws_create_ws).click()
        time.sleep(2)
        self.check_toast_message("WorkSpace created successfully")

        assert_that(self.browser.find_element(*ws.ws_title).text).is_equal_to("WS " + name)

    def edit_workspace(self):
        self.browser.find_element(*ws.ws_menu).click()
        self.browser.find_element(*ws.ws_menu_edit).click()
        today = date.today()
        now = datetime.now()
        day = today.strftime("%d-%m-%Y-")
        tm = now.strftime("%H-%M-%S")
        name = day + tm
        self.browser.find_element(*ws.ws_name).clear()
        self.browser.find_element(*ws.ws_name).send_keys("WS " + name)
        self.browser.find_element(*ws.ws_save).click()
        time.sleep(2)
        self.check_toast_message("WorkSpace updated successfully.")
        return "WS " + name

    def edit_workspace_outside_folder(self):
        self.browser.find_element(*d.d_workspace).click()
        name = self.edit_workspace()
        assert_that(self.browser.find_element(*ws.ws_title).text).is_equal_to(name)

    def edit_workspace_inside_folder(self):
        self.browser.find_element(*d.d_workspace).click()
        self.browser.find_element(*ws.ws_title).click()
        name = self.edit_workspace()
        ws_name = self.browser.find_element(*ws.ws_my_file_ws_title).text.split(f'\n')
        assert_that(ws_name[0]).is_equal_to(name)

    def delete_workspace(self, delete_files):
        self.browser.find_element(*ws.ws_menu).click()
        self.browser.find_element(*ws.ws_menu_delete).click()
        self.browser.find_element(*ws.ws_delete_cancel).click()

        self.browser.find_element(*ws.ws_menu).click()
        self.browser.find_element(*ws.ws_menu_delete).click()

        if delete_files.__eq__('yes'):
            self.browser.find_element(*ws.ws_delete_ws_files).click()

        self.browser.find_element(*ws.ws_delete).click()
        time.sleep(2)
        self.check_toast_message("WorkSpace deleted successfully.")
        assert_that(self.browser.find_element(*sloc.search_result_empty).text). \
            is_equal_to(cltxt.no_workspace_text)

    def delete_workspace_outside_folder(self, delete_file):
        self.browser.find_element(*d.d_workspace).click()
        self.delete_workspace(delete_file)

    def delete_workspace_inside_folder(self, delete_file):
        self.browser.find_element(*d.d_workspace).click()
        self.browser.find_element(*ws.ws_title).click()
        self.delete_workspace(delete_file)

    def check_workspace(self):
        with soft_assertions():
            workspace_name = self.browser.find_element(*ws.ws_title).text
            self.browser.find_element(*ws.ws_title).click()
            time.sleep(1)
            ws_name = self.browser.find_element(*ws.ws_my_file_ws_title).text.split(f'\n')
            assert_that(ws_name[0]).is_equal_to(workspace_name)
            self.browser.find_element(*ws.back_to_workspace).click()
            assert_that(self.browser.find_element(*ws.ws_title).text).is_equal_to(workspace_name)

    def search_template_inside_workspace(self):
        with soft_assertions():
            workspace_name = self.browser.find_element(*ws.ws_title).text
            self.browser.find_element(*ws.ws_title).click()
            time.sleep(1)
            ws_name = self.browser.find_element(*ws.ws_my_file_ws_title).text.split(f'\n')
            assert_that(ws_name[0]).is_equal_to(workspace_name)

            self.browser.find_element(*sloc.search_input).click()
            self.browser.find_element(*sloc.search_input).send_keys(cltxt.search_invalid_template)
            self.browser.find_element(*sloc.search_button).click()

            assert_that(self.browser.find_element(*sloc.search_result_empty).text).\
                is_equal_to(cltxt.search_template_not_found_in_ws_message)

            self.browser.find_element(*sloc.search_close_button).click()
            self.browser.find_element(*sloc.search_input).click()
            self.browser.find_element(*sloc.search_input).send_keys(cltxt.search_template)
            self.browser.find_element(*sloc.search_button).click()
            time.sleep(1)

            template_name = self.browser.find_element(*tloc.template_1_name).text

            assert_that(template_name).is_equal_to(cltxt.search_template)
            self.browser.find_element(*sloc.search_close_button).click()

    def add_template_to_workspace(self, source):
        self.browser.refresh()
        self.browser.find_element(*d.d_workspace).click()
        self.browser.find_element(*ws.ws_title).click()

        self.browser.find_element(*ws.add_template_to_ws).click()
        time.sleep(1)
        self.browser.find_element(*ws.add_template_to_ws_select_source).click()
        if source.__eq__('my_cloud'):
            self.browser.find_element(*ws.add_template_to_ws_select_source_my_cl).click()
        elif source.__eq__('workspace'):
            self.browser.find_element(*ws.add_template_to_ws_select_source_my_ws).click()
            time.sleep(1)
            self.browser.find_element(*ws.add_template_to_ws_select_ws).click()
            self.browser.find_element(*ws.add_template_to_ws_select_ws_0).click()
        else:
            self.browser.find_element(*ws.add_template_to_ws_select_source_sw).click()
            self.browser.find_element(*ws.add_template_to_ws_select_ws).click()
            self.browser.find_element(*ws.add_template_to_ws_select_ws_0).click()

        self.browser.find_element(*ws.add_template_to_ws_select_template).click()
        time.sleep(1)
        tmp_name = self.browser.find_element(*ws.add_template_to_ws_select_template_0).text
        self.browser.find_element(*ws.add_template_to_ws_select_template_0).click()
        time.sleep(1)
        self.browser.find_element(*ws.add_template_button).click()
        time.sleep(2)
        assert_that(self.browser.find_element(*tloc.template_1_name).text).is_equal_to(tmp_name)

    def share_workspace(self, email):
        self.browser.find_element(*ws.ws_share_with).click()
        self.browser.find_element(*ws.ws_share_with).clear()
        self.browser.find_element(*ws.ws_share_with).send_keys(email)
        self.browser.find_element(*ws.ws_email_add).click()
        self.browser.find_element(*ws.ws_email_remove).click()
        self.browser.find_element(*ws.ws_share_with).send_keys(email)
        self.browser.find_element(*ws.ws_save).click()

        self.check_toast_message('WorkSpace updated successfully.')

    def share_workspace_outside_folder(self, email):
        self.browser.refresh()
        self.browser.find_element(*d.d_workspace).click()
        self.browser.find_element(*ws.ws_share).click()
        self.share_workspace(email)

    def share_workspace_inside_folder(self, email):
        self.browser.refresh()
        self.browser.find_element(*d.d_workspace).click()
        self.browser.find_element(*ws.ws_title).click()
        self.browser.find_element(*ws.ws_my_file_ws_share).click()
        self.share_workspace(email)


class MyCloud(Helper, ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

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
        # Download
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

    def copy_to_workspace(self, platform):
        self.browser.find_element(*d.d_cloud).click()
        # Select platform
        self.select_platform(platform)
        # Template
        # template_name = self.browser.find_element(*tloc.template_1_name).text
        # Copy
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)
        self.browser.find_element(*tloc.template_1_menu_copy).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_0).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_done).click()

        self.check_toast_message('File copied to WorkSpace successfully')

    def move_to_workspace(self, platform):
        self.browser.find_element(*d.d_cloud).click()
        # Select platform
        self.select_platform(platform)
        # Template
        # template_name = self.browser.find_element(*tloc.template_1_name).text
        # Move
        self.browser.find_element(*tloc.template_1_menu).click()
        time.sleep(1)
        self.browser.find_element(*tloc.template_1_menu_move).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_0).click()
        self.browser.find_element(*tloc.copy_move_modal_select_ws_done).click()

        self.check_toast_message('File moved to WorkSpace successfully')

    def delete_template(self, platform):
        self.browser.find_element(*d.d_cloud).click()
        # Select platform
        self.select_platform(platform)
        # Template
        # template_name = self.browser.find_element(*tloc.template_1_name).text
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

    def search_template(self):
        with soft_assertions():
            self.browser.find_element(*d.d_cloud).click()
            self.browser.find_element(*sloc.search_input).click()
            self.browser.find_element(*sloc.search_input).send_keys(cltxt.search_invalid_template)
            self.browser.find_element(*sloc.search_button).click()
            assert_that(self.browser.find_element(*sloc.search_result_empty).text).\
                is_equal_to(cltxt.search_template_not_found_message)
            self.browser.find_element(*sloc.search_close_button).click()
            self.browser.find_element(*sloc.search_input).click()
            self.browser.find_element(*sloc.search_input).send_keys(cltxt.search_template)
            self.browser.find_element(*sloc.search_button).click()
            time.sleep(1)

            template_name = self.browser.find_element(*tloc.template_1_name).text

            assert_that(template_name).is_equal_to(cltxt.search_template)

    def change_layout(self, layout):
        if layout.__eq__('grid'):
            self.browser.find_element(*cl.view_grid).click()
            time.sleep(1)
            if not len(self.browser.find_elements(*tloc.template_1_date)) > 0:
                assert_that("Success").is_equal_to("Layout " + layout + "Not changed.")
        else:
            self.browser.find_element(*cl.view_list).click()
            if not len(self.browser.find_elements(*tloc.template_1_date)) > 0:
                assert_that("Success").is_equal_to("Layout " + layout + "Not changed.")


class SharedWithMe(ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)
