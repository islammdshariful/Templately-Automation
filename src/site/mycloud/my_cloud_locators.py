from selenium.webdriver.common.by import By


class DashboardLocators:
    title = (By.XPATH, f"//h4[normalize-space()='My Cloud']")

    # Profile Menu
    p_menu = (By.XPATH, f'//span[starts-with(@class, "Style_tly__user__details")]')
    p_menu_workspace = (By.XPATH, f"//div[starts-with(@class,'Style_tly__dropdown__menu__item')]//div//li[1]")
    p_menu_share = (By.XPATH, f"//div[starts-with(@class,'Style_tly__dropdown__menu__item')]//div//li[2]")
    p_menu_profile = (By.XPATH, f"//div[starts-with(@class,'Style_tly__dropdown__menu__item')]//div//li[3]")
    p_menu_api = (By.XPATH, f"//div[starts-with(@class,'Style_tly__dropdown__menu__item')]//div//li[4]")
    p_menu_subscription = (By.XPATH, f"//div[starts-with(@class,'Style_tly__dropdown__menu__item')]//div//li[5]")
    p_menu_signout = (By.XPATH, f"//a[starts-with(@class,'Style_tly__logout_button')]")

    # Dashboard Menu
    d_cloud = (By.XPATH, f"//span[normalize-space()='My Cloud']")
    d_workspace = (By.XPATH, f"//span[normalize-space()='My WorkSpace']")
    d_share = (By.XPATH, f"//span[normalize-space()='Shared with Me']")
    d_profile = (By.XPATH, f"//span[normalize-space()='Profile']")
    d_api = (By.XPATH, f"//span[normalize-space()='Manage APIs']")
    d_subscription = (By.XPATH, f"//span[normalize-space()='Subscription']")
    d_payment = (By.XPATH, f"//span[normalize-space()='Payment History']")


class MyWorkSpaceLocators:
    # My WorkSpace
    ws_add = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__cloud__card__LefI_ "
                        f"Style_tly__cloud__add__workspace__card')]")
    ws_name = (By.XPATH, f"//input[@placeholder='WorkSpace name']")
    ws_email = (By.XPATH, f"//input[@placeholder='Email Address']")
    ws_email_add = (By.XPATH, f"//button[normalize-space()='Add']")
    ws_email_remove = (By.XPATH, f"//span[@class='Style_tly__close_button__pnto8']")
    ws_create_ws = (By.XPATH, f"//span[normalize-space()='Create WorkSpace']")

    ws_title = (By.XPATH, f'//a[starts-with(@class, "Style_tly__cloud__workspace__title")]')
    ws_menu = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__dropdown__toggler__dot__KVslN')]")
    ws_menu_edit = (By.XPATH, f"//li[normalize-space()='Edit']")
    ws_menu_delete = (By.XPATH, f"//li[normalize-space()='Delete']")
    ws_save = (By.XPATH, f"//span[normalize-space()='Save']")
    ws_delete_cancel = (By.XPATH, f"//button[normalize-space()='Cancel']")
    ws_delete = (By.XPATH, f"//button[normalize-space()='Delete']")
    ws_delete_ws_files = (By.XPATH, f"//label[@for='condition']")


class MyCloudLocators:
    # Platform
    select_platform = (By.XPATH, f"//div[@id='react-select-2-placeholder']")
    platform_all = (By.ID, f'react-select-2-option-0')
    platform_gutenberg = (By.ID, f'react-select-2-option-1')
    platform_elementor = (By.ID, f'react-select-2-option-2')
    #
    # template_1_name = (By.XPATH, f"//body/div[@id='__next']/div[starts-with(@class, 'Style_template__wrapper')]"
    #                              f"/div/div/main/section[starts-with(@class, 'Style_tly__section')]/"
    #                              f"div[starts-with(@class, 'Hero_tly__section__content')]/"
    #                              f"div[starts-with(@class, 'Grid_tly__container__')]/div/"
    #                              f"div[starts-with(@class, 'Style_tly__cloud__body')]/"
    #                              f"div[starts-with(@class, 'Style_tly__cloud__content')]/"
    #                              f"div[starts-with(@class, 'Style_tly__cloud__box__')]/div[1]/div[1]/span[1]")
    template_1_name = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/div/section/div[3]/div/div/div[2]/div[2]/div/div/span')
    template_1_date = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__content')]//div[1]//div[1]//p[1]")
    template_1_menu = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__body')]//div[1]//div[1]//div[2]//"
                                 f"button[1]")
    template_1_menu_download = (By.XPATH, f"//span[normalize-space()='Download']")
    template_1_menu_copy = (By.XPATH, f"//span[normalize-space()='Copy to WorkSpace']")
    template_1_menu_move = (By.XPATH, f"//span[normalize-space()='Move to WorkSpace']")
    template_1_menu_delete = (By.XPATH, f"//span[normalize-space()='Delete']")

    copy_move_modal_select_ws = (By.XPATH, f"//div[@id='react-select-3-placeholder']")
    copy_move_modal_select_ws_0 = (By.ID, f'react-select-3-option-0')
    copy_move_modal_select_ws_1 = (By.ID, f'react-select-3-option-1')
    copy_move_modal_select_ws_done = (By.XPATH, f"//span[normalize-space()='Done']")

    delete_modal_title = (By.XPATH, f"//h4[normalize-space()='Are You Sure?']")
    delete_modal_des = (By.XPATH, f"//p[starts-with(@class, 'Modal_tly__body__message__')]")
    delete_modal_delete_button = (By.XPATH, f"//button[normalize-space()='Delete']")
    delete_modal_cancel_button = (By.XPATH, f"//button[normalize-space()='Cancel']")

    search_input = (By.XPATH, f"//input[@placeholder='Search here . . . .']")
    search_button = (By.XPATH, f"//button[contains(text(),'Search')]")
    search_close_button = (By.XPATH, f"//button[starts-with(@class, 'Style_search_close_button')]")

    search_result_empty = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__color__danger')]")


class MyCloudText:
    title_text = "My Cloud"
    search_template = "A1"
    search_invalid_template = "Dummy Search is given, Expecting No Result."
    search_template_not_found_message = "You do not have any item with '" + search_invalid_template + "' in title"
    # search_template_not_found_message = "You do not have any item with 'Dummy Search is given, Expecting No Result.' in title"
