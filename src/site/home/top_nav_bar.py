from selenium.webdriver.common.by import By


class TopNavBar:
    header_nav = "//nav[starts-with(@class,'Header_tly__header__navbar')]//div[2]"
    home = (By.XPATH, header_nav + "//ul//li[1]")
    browse = (By.XPATH, header_nav + "//ul//li[2]")
    browse_elementor = (By.XPATH, header_nav + "//ul//li[2]//span//ui//li[1]")
    menu_browse_gutenberg = (By.XPATH, header_nav + "//ul//li[2]//span//ul//li[2]")
    pricing = (By.XPATH, header_nav + "//ul//li[3]")
    doc = (By.XPATH, header_nav + "//ul//li[4]")
    blog = (By.XPATH, header_nav + "//ul//li[5]")
    my_cloud = (By.XPATH, header_nav + f"//a")
    sign_in_profile = (By.XPATH, header_nav + f"//div")

    def __init__(self, browser):
        self.browser = browser

    def click_home(self):
        self.browser.find_element(*self.home).click()

    def click_browse(self):
        self.browser.find_element(*self.browse).click()

    def click_pricing(self):
        self.browser.find_element(*self.pricing).click()

    def click_doc(self):
        self.browser.find_element(*self.doc).click()

    def click_blog(self):
        self.browser.find_element(*self.blog).click()

    def click_my_cloud(self):
        self.browser.find_element(*self.my_cloud).click()

    def click_sign_in(self):
        self.browser.find_element(*self.sign_in_profile).click()

    def click_profile_menu(self):
        self.browser.find_element(*self.sign_in_profile).click()

