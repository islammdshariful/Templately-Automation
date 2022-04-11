from assertpy import assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from src.site.dashboard.dashboard_locators import DashboardLocators as d
from src.site.home.home_page_locators import HomePageLocators as hloc
from src.site.home.home_page_locators import HomePageTexts as htxt

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:
    def __init__(self, browser):
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self, url):
        self.browser.get(url)

    def sign_out(self):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[starts-with(@class, 'Style_tly__button')]")))
        element.click()
        # self.browser.find_element(*hloc.my_cloud_btn).click()
        self.browser.find_element(*d.p_menu).click()
        self.browser.find_element(*d.p_menu_signout).click()
        assert_that(self.browser.find_element(*hloc.header).text).is_equal_to(htxt.header_txt)