from assertpy import assert_that
from selenium.webdriver.common.by import By
from utils.configuration import Config


class CheckText:
    def __init__(self, browser):
        self.browser = browser
        self.conf = Config()

    def check_title(self, text):
        assert_that(self.browser.title).is_equal_to(text)


class CheckVisibility:
    def __init__(self, browser):
        self.browser = browser

    def check_visibility(self, elem, err_text):
        if self.browser.find_element(By.XPATH, elem).is_displayed():
            assert_that(1).is_equal_to(1)
        else:
            assert_that(1).is_equal_to(err_text)
