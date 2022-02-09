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
    # WorkSpace Folder
    ws_title = (By.XPATH, f'//a[starts-with(@class, "Style_tly__cloud__workspace__title")]')
    ws_menu = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__dropdown__toggler__dot')]")
    ws_menu_edit = (By.XPATH, f"//li[normalize-space()='Edit']")
    ws_menu_delete = (By.XPATH, f"//li[normalize-space()='Delete']")
    ws_save = (By.XPATH, f"//span[normalize-space()='Save']")
    ws_delete_cancel = (By.XPATH, f"//button[normalize-space()='Cancel']")
    ws_delete = (By.XPATH, f"//button[normalize-space()='Delete']")
    ws_delete_ws_files = (By.XPATH, f"//label[@for='condition']")
    # In WorkSpace Folder
    ws_my_file_ws_title = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__workspace__title')]")
    ws_my_file_ws_user = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__workspace__title')]/span")
    ws_my_file_ws_share = (By.XPATH, f"//ul[starts-with(@class, 'Style_tly__cloud__share__list')]")
    ws_my_file_ws_menu = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__header')]//button[@type='button']")
    # Back to My WorkSpace
    back_to_workspace = (By.XPATH, f"//a[starts-with(@class, 'Style_tly__back__button')]")
    # Search
    select_workspace = (By.XPATH, f"//div[@id='searchWorkspace']")
    select_workspace_ws_0 = (By.ID, f'react-select-searchWorkspace-option-0')
    select_workspace_ws_1 = (By.ID, f'react-select-searchWorkspace-option-1')

    search_input = (By.XPATH, f"//input[@placeholder='Search here . . . .']")
    search_button = (By.XPATH, f"//button[normalize-space()='Search']")
    # Add Template
    add_template_to_ws = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__view__toggler')]//button[1]")
    # Source
    add_template_to_ws_select_source = (By.XPATH, f"//div[@id='react-select-4-placeholder']")
    add_template_to_ws_select_source_my_cl = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                        f"//div[1]")
    add_template_to_ws_select_source_my_ws = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                        f"//div[2]")
    add_template_to_ws_select_source_sw = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                     f"//div[3]")
    # WorkSpace
    add_template_to_ws_select_ws = (By.XPATH, f"//div[@id='react-select-6-placeholder']")
    add_template_to_ws_select_ws_0 = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                f"//div[1]")
    add_template_to_ws_select_ws_1 = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                f"//div[2]")
    # Template
    add_template_to_ws_select_template = (By.XPATH, f"//div[@id='react-select-5-placeholder']")
    add_template_to_ws_select_template_4 = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                      f"//div[4]")
    add_template_button = (By.XPATH, f"//span[normalize-space()='Add to WorkSpace']")

    # Layout view
    view_grid = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__view__toggler')]//button[2]")
    view_list = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__view__toggler')]//button[3]")


class TemplateLocators:
    # Template
    template_1_name = (By.XPATH, f"//span[starts-with(@class, 'Style_tly__cloud__card__title')]")
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


class SearchTemplateLocators:
    search_input = (By.XPATH, f"//input[@placeholder='Search here . . . .']")
    search_button = (By.XPATH, f"//button[contains(text(),'Search')]")
    search_close_button = (By.XPATH, f"//button[starts-with(@class, 'Style_search_close_button')]")

    search_result_empty = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__color__danger')]")


class MyCloudLocators:
    # Platform
    select_platform = (By.XPATH, f"//div[@id='react-select-2-placeholder']")
    platform_all = (By.ID, f'react-select-2-option-0')
    platform_gutenberg = (By.ID, f'react-select-2-option-1')
    platform_elementor = (By.ID, f'react-select-2-option-2')

    view_grid = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__view__toggler')]//button[1]")
    view_list = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__view__toggler')]//button[2]")


class MyCloudText:
    title_text = "My Cloud"
    search_template = "A1"
    search_invalid_template = "Dummy Search is given, Expecting No Result."
    search_template_not_found_message = "You do not have any item with '" + search_invalid_template + "' in title"
    search_template_not_found_in_ws_message = "No files found in this WorkSpace."
