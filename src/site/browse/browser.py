import time

from assertpy import soft_assertions, assert_that
from selenium.webdriver import Keys

from src.site.home.top_nav_bar import TopNavBar
from utils.helper import Helper
from src.site.browse.browse_locators import BrowserSearchSectionLocators as search
from src.site.browse.browse_locators import AppliedFiltersLocators as filters


class BrowseTemplates(TopNavBar):
    def __init__(self, browser):
        super().__init__(browser)

    def load(self):
        self.browser.get()

    def search_with_popular_keys(self):
        self.click_browse()
        self.browser.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        search_key = self.browser.find_element(*search.popular_search_1)
        search_key.click()
        time.sleep(1)

        assert_that(self.browser.find_element(*filters.applied_filter_label).text).is_equal_to("Applied Filters:")
        assert_that(self.browser.find_element(*filters.applied_filter_1).text).is_equal_to("Pack:\nAll Packs")
        assert_that(self.browser.find_element(*filters.applied_filter_2).text).is_equal_to(search_key.text.lower())

        self.browser.find_element(*filters.clear_all_button).click()
        time.sleep(1)
        if len(self.browser.find_elements(*filters.applied_filter_label)) > 0:
            assert_that("Success").is_equal_to("'Clear All' button not clearing the fields")
        else:
            assert_that(1).is_equal_to(1)
        search_key.click()

    def testcase(self):
        with soft_assertions():
            self.search_with_popular_keys()
