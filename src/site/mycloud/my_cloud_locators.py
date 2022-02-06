from selenium.webdriver.common.by import By


class MyCloudLocators:
    title = (By.XPATH, f"//h4[@class='Style_tly__cloud__content__title__52RgC']")

    # Profile Menu
    p_menu = (By.XPATH, f'//*[@id="__next"]/div[3]/header/div[3]/div/nav/div[2]/div/div/button/span[1]')
    p_menu_workspace = (By.XPATH, f'//*[@id="__next"]/div[3]/header/div[3]/div/nav/div[2]/div/div/div/ul/li[1]')
    p_menu_share = (By.XPATH, f'//*[@id="__next"]/div[3]/header/div[3]/div/nav/div[2]/div/div/div/ul/li[1]')
    p_menu_profile = (By.XPATH, f'//*[@id="__next"]/div[3]/header/div[3]/div/nav/div[2]/div/div/div/ul/li[1]')
    p_menu_api = (By.XPATH, f'//*[@id="__next"]/div[3]/header/div[3]/div/nav/div[2]/div/div/div/ul/li[1]')
    p_menu_subscription = (By.XPATH, f'//*[@id="__next"]/div[3]/header/div[3]/div/nav/div[2]/div/div/div/ul/li[1]')
    p_menu_signout = (By.XPATH, f'//*[@id="__next"]/div[3]/header/div[3]/div/nav/div[2]/div/div/div/div')

    # Dashboard Menu
    d_cloud = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[1]/ul/li[1]/a/span[2]')
    d_workspace = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[1]/ul/li[2]/a/span[2]')
    d_share = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[1]/ul/li[3]/a/span[2]')
    d_profile = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[1]/ul/li[4]/a/span[2]')
    d_api = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[1]/ul/li[5]/a/span[2]')
    d_subscription = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[1]/ul/li[6]/a/span[2]')
    d_payment = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[1]/ul/li[7]/a/span[2]')

    # My WorkSpace
    ws_add = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[2]/div[2]/button')
    ws_name = (By.XPATH, f"//input[@placeholder='WorkSpace name']")
    ws_email = (By.XPATH, f"//input[@placeholder='Email Address']")
    ws_email_add = (By.XPATH, f"//button[normalize-space()='Add']")
    ws_email_remove = (By.XPATH, f"/html/body/div[4]/div/div/div[1]/div[2]/div[1]/p/span[2]")
    ws_create_ws = (By.XPATH, f"//span[normalize-space()='Create WorkSpace']")

    ws_title = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[2]/div[2]/div/div/a[2]')
    ws_menu = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[2]/div[2]/div/div/div[2]')
    ws_menu_edit = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[2]/div[2]/div/div'
                              f'/div[2]/div/span/span/span/ul/li[1]')
    ws_menu_delete = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div/section/div[3]/div/div/div[2]/div[2]/div/div'
                                f'/div[2]/div/span/span/span/ul/li[2]')
    ws_save = (By.XPATH, f"//span[normalize-space()='Save']")
    ws_delete_cancel = (By.XPATH, f"//button[normalize-space()='Cancel']")
    ws_delete = (By.XPATH, f"//button[normalize-space()='Delete']")
    ws_delete_ws_files = (By.XPATH, f"/html/body/div[8]/div/div/div[1]/div[1]/label/span")


class MyCloudText:
    title_text = "My Cloud"
