from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import ToastMessage, Helper
from src.site.dashboard.dashboard_locators import MyWorkSpaceLocators as ws
from src.site.dashboard.dashboard_locators import DashboardLocators as d
from src.site.dashboard.dashboard_locators import SearchTemplateLocators as sloc
from src.site.dashboard.dashboard_locators import TemplateLocators as tloc
from src.site.dashboard.dashboard_locators import MyCloudText as cltxt
from datetime import date, datetime
import time


class MyWorkSpace(ToastMessage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def create_workspace(self, add_people_email):
        self.browser.find_element(*d.d_workspace).click()
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, ws.ws_add)))
        # self.browser.find_element(*ws.ws_add).click()
        element.click()
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

    def check_template_inside_workspace(self, name):
        self.browser.find_element(*d.d_workspace).click()
        self.browser.find_element(*ws.ws_title).click()
        template_name = self.browser.find_element(*tloc.template_1_name).text

        if not template_name.__eq__(name):
            assert_that("success").is_equal_to("Template name not matched")

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

    def search_template_inside_workspace(self, query):
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
            self.browser.find_element(*sloc.search_input).send_keys(query)
            self.browser.find_element(*sloc.search_button).click()
            time.sleep(1)

            template_name = self.browser.find_element(*tloc.template_1_name).text

            assert_that(template_name).is_equal_to(query)
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

