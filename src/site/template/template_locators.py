from selenium.webdriver.common.by import By


class TemplateLocators:
    title = (By.XPATH, f"//h3[starts-with(@class, 'SingleView_tly__panel__title')]")
    category = (By.XPATH, f"//p[starts-with(@class, 'SingleView_tly__meta__data')]//span")
    category_name = (By.XPATH, f"//p[starts-with(@class, 'SingleView_tly__meta__data')]//a")
    img_cat = (By.XPATH, f"//div[starts-with(@class, 'SingleView_tly__single__product__preview')]//div[1]//span")
    img_cat_for_page = (By.XPATH, f"//div[starts-with(@class, 'SingleView_tly__single__product__preview')]//div[2]//span")
    favourite_icon = f"//i[starts-with(@class, 'ticon t-heart')]"
    favourite_count = (By.XPATH, f"//div[starts-with(@class, 'SingleView_tly__favorite__ratting')]//span[2]")
    download_icon = f"//i[starts-with(@class, 'ticon t-download')]"
    download_count = (By.XPATH, f"//div[starts-with(@class, 'SingleView_tly__download__ratting')]//span[2]")
    ratings_icon = f"//i[starts-with(@class, 'ticon t-star')]"
    ratings_count = (By.XPATH, f"//div[starts-with(@class, 'SingleView_tly__star__count')]//span[2]")
    submit_ratings_box = f"//ul[starts-with(@class, 'SingleView_tly__rate__with__star')]"

class TemplateTexts:
        title = ""