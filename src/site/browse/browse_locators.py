from selenium.webdriver.common.by import By


class BrowseLocators:
    header = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/section/div[2]/div')


class BrowseText:
    header_txt = "READY TO IMPORT\nWordPress Templates"