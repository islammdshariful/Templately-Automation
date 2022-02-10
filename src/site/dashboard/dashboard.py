from assertpy import assert_that
from selenium.webdriver import ActionChains
from src.site.dashboard.dashboard_locators import DashboardLocators as d
from src.site.home.home_page_locators import HomePageLocators as hloc
from src.site.home.home_page_locators import HomePageTexts as htxt


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