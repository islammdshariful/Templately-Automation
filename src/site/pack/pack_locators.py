from selenium.webdriver.common.by import By


class PackLocators:
    title = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[3]/div/h3')
    category = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/p/span')
