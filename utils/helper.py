from assertpy import assert_that
from selenium.webdriver.common.by import By


class Helper:
    def __init__(self, browser):
        self.browser = browser

    def check_title(self, text):
        assert_that(self.browser.title).is_equal_to(text)

    def check_visibility(self, elem, err_text):
        if self.browser.find_element(By.XPATH, elem).is_displayed():
            assert_that(1).is_equal_to(1)
        else:
            assert_that(1).is_equal_to(err_text)


class ToastMessage:
    title = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/div[1]/div[2]')
    cross = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/button')

    def __init__(self, browser):
        self.browser = browser

    def check_toast_message(self, message):
        assert_that(self.browser.find_element(*self.title).text).is_equal_to(message)
        self.browser.find_element(*self.cross).click()
