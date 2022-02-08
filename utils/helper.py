import time

from assertpy import assert_that, soft_assertions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:
    file_path = 'C:\\Users\\shari\\'
    bar_close_button = (By.XPATH, f'//*[@id="__next"]/div[2]/button')

    def __init__(self, browser):
        self.browser = browser

    def check_title(self, text):
        assert_that(self.browser.title).is_equal_to(text)

    def check_visibility(self, elem, err_text):
        if self.browser.find_element(By.XPATH, elem).is_displayed():
            assert_that(1).is_equal_to(1)
        else:
            assert_that(1).is_equal_to(err_text)

    def close_bar(self):
        time.sleep(1)
        if len(self.browser.find_elements(*self.bar_close_button)) > 0:
            self.browser.find_element(*self.bar_close_button).click()


class ToastMessage:
    toast_title = f"//div[@role='alert']"
    cross = (By.XPATH, f"//button[@aria-label='close']//*[name()='svg']")

    def __init__(self, browser):
        self.browser = browser

    def check_toast_message(self, message):
        with soft_assertions():
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, self.toast_title)))
            time.sleep(2)
            assert_that(self.browser.find_element(By.XPATH, self.toast_title).text).is_equal_to(message)
            self.browser.find_element(*self.cross).click()
