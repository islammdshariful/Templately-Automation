from selenium.webdriver.common.by import By


class TemplateLocators:
    title = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[3]/div/h3')
    category = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/p/span')
    category_name = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/p/a')
    img_cat = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[1]/div[1]/div[1]/div/span')
    favourite_icon = f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/div[1]/div[1]/span[2]'
    favourite_count = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/div[1]'
                                 f'/div[1]/span[2]')
    download_icon = f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/div[1]/div[2]/span[1]/i'
    download_count = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/div[1]'
                                f'/div[2]/span[2]')
    ratings_icon = f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/div[2]/div[1]/span[1]/i'
    ratings_count = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/div[2]'
                               f'/div[1]/span[2]')
    submit_ratings_box = f'//*[@id="__next"]/div[3]/div/div/main/section[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/ul'

class TemplateTexts:
        title = ""