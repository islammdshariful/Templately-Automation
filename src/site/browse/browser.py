import time

from assertpy import soft_assertions, assert_that
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from numerize import numerize

from src.site.home.top_nav_bar import TopNavBar
from src.site.template.template import Template
from utils.helper import Helper
from src.site.browse.browse_locators import BrowserSearchSectionLocators as search
from src.site.browse.browse_locators import AppliedFiltersLocators as filters
from src.site.browse.browse_locators import Templates as tmp


class BrowseTemplates(TopNavBar, Template):
    def __init__(self, browser):
        super().__init__(browser)
        self.cursor = ActionChains(self.browser)

    def load(self):
        self.browser.get()

    def clear_all_filter(self):
        self.browser.find_element(*filters.clear_all_button).click()
        time.sleep(1)
        if len(self.browser.find_elements(*filters.applied_filter_label)) > 0:
            assert_that("Success").is_equal_to("'Clear All' button not clearing the fields")
        else:
            assert_that(1).is_equal_to(1)

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

        self.clear_all_filter()
        search_key.click()
        time.sleep(1)
        self.clear_all_filter()

    def check_search_input_field(self, query):
        # This is checking the search input field
        self.click_browse()
        self.browser.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)
        self.browser.find_element(*search.search_field).click()
        self.browser.find_element(*search.search_field).send_keys(query)
        time.sleep(1)
        text = self.browser.find_element(*search.search_field).get_attribute("value")
        assert_that(text).is_equal_to(query)
        self.browser.find_element(*search.search_close_button).click()
        time.sleep(1)
        text = self.browser.find_element(*search.search_field).get_attribute("value")
        assert_that(text).is_equal_to("")

    def search_query(self, query):
        self.browser.find_element(*search.search_field).click()
        self.browser.find_element(*search.search_field).clear()
        self.browser.find_element(*search.search_field).send_keys(query)
        time.sleep(1)
        self.browser.find_element(*search.search_button).click()
        time.sleep(1)

    def search_template(self, query):
        self.click_browse()
        self.search_query(query)
        assert_that(self.browser.find_element(*filters.applied_filter_label).text).is_equal_to("Applied Filters:")
        assert_that(self.browser.find_element(*filters.applied_filter_1).text).\
            is_equal_to('Search Text: "' + query.lower() + '"')

        self.check_template_via_other_page(tmp.template_1_slug_from_title, tmp.template_1_ratings,
                                           tmp.template_1_ratings_icon, tmp.template_1_download,
                                           tmp.template_1_download_icon, tmp.template_1_category,
                                           tmp.template_1_category_from_img)

        self.clear_all_filter()
        self.search_query(query)

        assert_that(self.browser.find_element(*filters.applied_filter_label).text).is_equal_to("Applied Filters:")
        assert_that(self.browser.find_element(*filters.applied_filter_1).text).\
            is_equal_to('Search Text: "' + query.lower() + '"')

        self.check_template_via_other_page(tmp.template_9_slug_from_title, tmp.template_9_ratings,
                                           tmp.template_9_ratings_icon, tmp.template_9_download,
                                           tmp.template_9_download_icon, tmp.template_9_category,
                                           tmp.template_9_category_from_img)
        self.clear_all_filter()

    def test_me(self):
        text = self.browser.find_element(By.XPATH, tmp.template_1_download).text
        normalize_downloads_txt = numerize.numerize(int(text))
        print(normalize_downloads_txt)

    def testcase(self):
        with soft_assertions():
            self.search_with_popular_keys()
            # self.search_template("book store")
            # self.test_me()
