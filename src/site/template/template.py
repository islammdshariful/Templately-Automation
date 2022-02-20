import time

from assertpy import assert_that
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from src.site.template.template_locators import TemplateLocators as loc

from utils.helper import Helper


class Template(Helper):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.cursor = ActionChains(self.browser)

    def load(self):
        self.browser.get()

    def check_template_via_other_page(self, title, rate, rate_icon, download, download_icon, category, cat_img):
        ratings_txt = self.browser.find_element(By.XPATH, rate).text
        downloads_txt = self.browser.find_element(By.XPATH, download).text
        ttl_txt = self.browser.find_element(By.XPATH, title).text
        cat_txt = self.browser.find_element(By.XPATH, category).text
        cat_frm_img_txt = self.browser.find_element(By.XPATH, cat_img).text

        self.check_visibility(rate_icon, "Ratings icon is not visible")
        self.check_visibility(download_icon, "Download icon is not visible")

        self.cursor.move_to_element(self.browser.find_element(By.XPATH, title)).perform()
        time.sleep(1)
        self.browser.find_element(By.XPATH, title).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*loc.title).text).is_equal_to(ttl_txt)
        time.sleep(1)
        assert_that(self.browser.find_element(*loc.download_count).text).is_equal_to(downloads_txt)
        assert_that(self.browser.find_element(*loc.ratings_count).text).is_equal_to(ratings_txt)

        if cat_txt == cat_frm_img_txt:
            assert_that(self.browser.find_element(*loc.img_cat).text).is_equal_to(cat_txt)
        else:
            assert_that(self.browser.find_element(*loc.img_cat).text).is_equal_to(cat_frm_img_txt)

        self.check_visibility(loc.favourite_icon, "Favourite icon is not visible")
        self.check_visibility(loc.download_icon, "Download icon is not visible")
        self.check_visibility(loc.ratings_icon, "Ratings icon is not visible")
        self.check_visibility(loc.submit_ratings_box, "Rating Box is not visible")
        self.browser.back()
        time.sleep(1)

    def check_template(self, category, title, price, cat, rate, down):
        assert_that(self.browser.find_element(*loc.title).text).is_equal_to(title)
        assert_that(self.browser.find_element(*loc.img_cat).text).is_equal_to(price)
        if not category.__eq__('page'):
            assert_that(self.browser.find_element(*loc.category_name).text.upper()).is_equal_to(cat)
        time.sleep(2)
        assert_that(self.browser.find_element(*loc.ratings_count).text).is_equal_to(rate)
        assert_that(self.browser.find_element(*loc.download_count).text).is_equal_to(down)

        self.check_visibility(loc.favourite_icon, "Favourite icon is not visible")
        self.check_visibility(loc.download_icon, "Download icon is not visible")
        self.check_visibility(loc.ratings_icon, "Ratings icon is not visible")
        self.check_visibility(loc.submit_ratings_box, "Rating Box is not visible")
        self.browser.back()
        time.sleep(1)

    def check_template_title(self, title):
        assert_that(self.browser.find_element(*loc.title).text).is_equal_to(title)
        self.browser.back()
        time.sleep(1)
