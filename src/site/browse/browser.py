from assertpy import soft_assertions
from selenium.webdriver import ActionChains

from utils.config import *
from utils.helper import CheckText


class Name:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get()

    def testcase(self):
        c = CheckText(self.browser)
        with soft_assertions():
            c.check_title(txt.title)

            self.browser.execute_script("window.scrollTo(0, 905)")
