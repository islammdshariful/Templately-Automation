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
    ws_email_remove = (By.XPATH, f"//span[starts-with(@class, 'Style_tly__close_button')]")
    ws_create_ws = (By.XPATH, f"//span[normalize-space()='Create WorkSpace']")
    # WorkSpace Folder
    ws_title = (By.XPATH, f'//a[starts-with(@class, "Style_tly__cloud__workspace__title")]')
    ws_share = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__cloud__share__list__item')]")
    ws_share_with = (By.XPATH, f"//div[starts-with(@class, 'Grid_tly__d_flex')]//input")
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
    add_template_to_ws_select_source = (By.XPATH, f"//div[normalize-space()='Select Source']")
    add_template_to_ws_select_source_my_cl = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                        f"//div[1]")
    add_template_to_ws_select_source_my_ws = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                        f"//div[2]")
    add_template_to_ws_select_source_sw = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                     f"//div[3]")
    # WorkSpace
    add_template_to_ws_select_ws = (By.XPATH, f"//div[normalize-space()='Select WorkSpace']")
    add_template_to_ws_select_ws_0 = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                f"//div[1]")
    add_template_to_ws_select_ws_1 = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                f"//div[2]")
    # Template
    add_template_to_ws_select_template = (By.XPATH, f"//div[normalize-space()='Select Templates']")
    add_template_to_ws_select_template_0 = (By.XPATH, f"//div[starts-with(@Class, 'react-select__menu-list')]"
                                                      f"//div[2]")
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


class ProfileLocators:
    # Profile Menu
    profile_info = (By.XPATH, f"//span[normalize-space()='Personal Info']")
    change_pass = (By.XPATH, f"//span[normalize-space()='Change Password']")
    payment_method = (By.XPATH, f"//span[normalize-space()='Payment Method']")
    my_favorites = (By.XPATH, f"//span[normalize-space()='My Favorites']")
    my_download = (By.XPATH, f"//span[normalize-space()='My Downloads']")

    # Profile Info
    browse_image = (By.XPATH, f"//label[starts-with(@class, 'Style_tly__image__browse__button')]")
    input_image = (By.ID, f'myFile')
    image_apply = (By.XPATH, f"//button[normalize-space()='Apply']")
    image_remove = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__image__preview__remove')]")
    upload_button = (By.XPATH, f"//label[normalize-space()='Upload']")
    remove_button = (By.XPATH, f"//button[normalize-space()='Remove']")
    first_name = (By.XPATH, f"//input[@placeholder='First Name....']")
    last_name = (By.XPATH, f"//input[@placeholder='Last Name....']")
    email = (By.XPATH, f"//input[@placeholder='Primary Email....']")
    update_button = (By.XPATH, f"//button[normalize-space()='Update']")
    email_update_notice = (By.XPATH, "//p[contains(text(),'Your profile is updated successfully')]")
    # Change Password
    current_pass = (By.XPATH, f"//input[@id='currentpassword']")
    new_pass = (By.XPATH, f"//input[@id='newpassword']")
    con_new_pass = (By.XPATH, f"//input[@id='confirmpassword']")
    change_pass_button = (By.XPATH, f"//button[normalize-space()='Change Password']")
    # Payment Method
    add_card = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__payment__method__card')]")
    back_to_dashboard = (By.XPATH, f"//img[@alt='Templately logo']")
    go_to_home = (By.XPATH, f"//a[normalize-space()='Go to home']")
    # Stripe
    stripe_email = (By.XPATH, f"//input[@id='email']")
    stripe_card_number = (By.XPATH, f"//input[@id='cardNumber']")
    stripe_card_expiry_date = (By.XPATH, f"//input[@id='cardExpiry']")
    stripe_card_cvc_number = (By.XPATH, f"//input[@id='cardCvc']")
    stripe_card_name = (By.XPATH, f"//input[@id='billingName']")
    save_card = (By.XPATH, f"//button[@type='submit']")
    # Card
    set_card_as_default = (By.XPATH, f"//span[normalize-space()='Set as Default']")
    delete_card = (By.XPATH, f"//div[starts-with(@class,'Style_tly__payment__method__card__wrapper')]//div[1]//div[2]"
                             f"//div[1]//button[1]//span[2]")
    set_new_card_as_default = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__payment__method__card__wrapper')]"
                                         f"//div[2]//div//button[2]//span")
    delete_card_2 = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__payment__method__card__wrapper')]"
                               f"//div[2]//div//button[1]")
    # Success page
    success_title = (By.XPATH, f"//h4[normalize-space()='Added Card Successfully']")
    success_des = (By.XPATH, f"//p[normalize-space()='You have successfully added card in Stripe']")

    # My Favorites
    price_select = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__filter')]//div[1]//button[1]")
    price_select_all = (By.XPATH, f"//div[normalize-space()='All']")
    price_select_starter = (By.XPATH, f"//div[contains(text(),'Starter')]")
    price_select_pro = (By.XPATH, f"//div[contains(text(),'Pro')]")
    category_select = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__cloud__filter')]//div[2]//button[1]")
    category_select_all = (By.XPATH, f"//div[normalize-space()='All']")
    category_select_blocks = (By.XPATH, f"//div[contains(text(),'Blocks')]")
    category_select_pages = (By.XPATH, f"//div[contains(text(),'Pages')]")
    category_select_packs = (By.XPATH, f"//div[contains(text(),'Packs')]")

    price_on_template = (By.XPATH, f"//div[starts-with(@class, 'Grid_tly__row__gutter__md__cols__2')]//div[1]//div//div"
                                   f"//a//div//div//span")
    image_on_template = f"//div[starts-with(@class, 'Grid_tly__row__gutter__md__cols__2')]//div[1]//div//div//a//div" \
                        f"//span//img"
    ratings_on_template = (By.XPATH, f"//div[starts-with(@class, 'Grid_tly__row__gutter__md__cols__2')]//div[1]//div"
                                     f"//div//div//div[1]//button//span[2]")
    downloads_on_template = (By.XPATH, f"//div[starts-with(@class, 'Grid_tly__row__gutter__md__cols__2')]//div[1]//div"
                                       f"//div//div//div[2]")
    category_on_template = (By.XPATH, f"//div[starts-with(@class, 'Grid_tly__row__gutter__md__cols__2')]//div[1]//div"
                                      f"//div//div//div[3]")
    title_on_template = (By.XPATH, f"//div[starts-with(@class, 'Grid_tly__row__gutter__md__cols__2')]//div[1]//div//div"
                                   f"//a[2]//h4")

    # My Downloads
    temp_1_thumbnail = f"//tbody[starts-with(@class, 'Table_tly__table_body')]//tr[1]//td[1]//span//span//img"
    temp_1_item_name = (By.XPATH, f"//tbody[starts-with(@class, 'Table_tly__table_body')]//tr[1]//td[2]")
    temp_1_download_date = (By.XPATH, f"//tbody[starts-with(@class, 'Table_tly__table_body')]//tr[1]//td[3]")


class ManageAPIsLocators:
    token_name = (By.XPATH, f"//input[@placeholder='Pick something cool, short and catchy!']")
    terms_of_services = (By.XPATH, f"//label[@for='condition']")
    create_token = (By.XPATH, f"//button[normalize-space()='Create Token']")
    # Modal
    copy_token = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__color__primary')]//i[@class='ticon t-duplicate']")
    token_label = f"//span[starts-with(@class, 'Style_tly__color__primary')]"
    registered_token = f"//span[starts-with(@style, 'word-break: break-word;')]"
    token_copied_condition = (By.XPATH, f"//span[contains(text(),'I confirm that I have copied this key and stored i')]")
    wahoo_got_it_btn = (By.XPATH, f"//span[normalize-space()='Wahoo! got it']")

    # API Token List
    token_1_name = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__row')]//div[1]")
    token_1_api_key = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__row')]//div[2]")
    token_1_active_sites = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__row')]//div[3]")

    token_1_copy = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__row')]//div[2]//div//span[2]//i")
    token_1_delete = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__row')]//div[2]//div//span[3]//i")

    # Delete Token Modal
    delete_modal_cancel = (By.XPATH, f"//button[normalize-space()='Cancel']")
    delete_modal_delete = (By.XPATH, f"//button[normalize-space()='Delete']")


class SubscriptionLocators:
    toggle_monthly = (By.XPATH, f"//button[@type='button'][normalize-space()='Monthly']")
    toggle_annual = (By.XPATH, f"//button[@type='button'][normalize-space()='Annual']")
    # Starter
    monthly_pack_starter = f"//div[starts-with(@class, 'Pricing_tly__pricing__card__container_2')]//div[1]//div"

    monthly_pack_starter_icon = monthly_pack_starter + f"//div[1]//div[1]//i"
    monthly_pack_starter_title = monthly_pack_starter + f"//div[1]//div[2]//h5"
    monthly_pack_starter_price = monthly_pack_starter + f"//div[1]//div[2]//p"

    monthly_pack_starter_des = "(" + monthly_pack_starter + f"//div[2])[2]"
    monthly_pack_starter_des_temp_count = monthly_pack_starter + f"//div[2]//p//span//a"
    monthly_pack_starter_des_item_1_icon = monthly_pack_starter + f"//div[2]//ul//li[1]/i"
    monthly_pack_starter_des_item_1_title = monthly_pack_starter + f"//div[2]//ul//li[1]"
    monthly_pack_starter_des_item_2_icon = monthly_pack_starter + f"//div[2]//ul//li[2]/i"
    monthly_pack_starter_des_item_2_title = monthly_pack_starter + f"//div[2]//ul//li[2]"
    monthly_pack_starter_des_item_3_icon = monthly_pack_starter + f"//div[2]//ul//li[3]/i"
    monthly_pack_starter_des_item_3_title = monthly_pack_starter + f"//div[2]//ul//li[3]"

    monthly_pack_starter_status = monthly_pack_starter + f"div[3]//button"
    # Premium
    premium_pack_starter = f"//div[starts-with(@class, 'Pricing_tly__pricing__card__container_2')]//div[2]//div"

    premium_pack_starter_icon = premium_pack_starter + f"//div[1]//div[1]//i"
    premium_pack_starter_title = premium_pack_starter + f"//div[1]//div[2]//h5"
    premium_pack_starter_price = premium_pack_starter + f"//div[1]//div[2]//p"

    premium_pack_starter_des = "(" + premium_pack_starter + f"//div[2])[2]"
    premium_pack_starter_des_temp_count = premium_pack_starter + f"//div[2]//p//span//a"
    premium_pack_starter_des_item_1_icon = premium_pack_starter + f"//div[2]//ul//li[1]/i"
    premium_pack_starter_des_item_1_title = premium_pack_starter + f"//div[2]//ul//li[1]"
    premium_pack_starter_des_item_2_icon = premium_pack_starter + f"//div[2]//ul//li[2]/i"
    premium_pack_starter_des_item_2_title = premium_pack_starter + f"//div[2]//ul//li[2]"

    premium_pack_starter_status = premium_pack_starter + f"div[3]//button"
    # Lifetime
    lifetime_pack_starter = f"//div[starts-with(@class, 'Pricing_tly__pricing__card__container_2')]//div[3]//div"

    lifetime_pack_starter_icon = lifetime_pack_starter + f"//div[1]//div[1]//i"
    lifetime_pack_starter_title = lifetime_pack_starter + f"//div[1]//div[2]//h5"
    lifetime_pack_starter_price = lifetime_pack_starter + f"//div[1]//div[2]//p"

    lifetime_pack_starter_des = "(" + lifetime_pack_starter + f"//div[2])[2]"
    lifetime_pack_starter_des_temp_count = lifetime_pack_starter + f"//div[2]//p//span//a"
    lifetime_pack_starter_des_item_1_icon = lifetime_pack_starter + f"//div[2]//ul//li[1]/i"
    lifetime_pack_starter_des_item_1_title = lifetime_pack_starter + f"//div[2]//ul//li[1]"
    lifetime_pack_starter_des_item_2_icon = lifetime_pack_starter + f"//div[2]//ul//li[2]/i"
    lifetime_pack_starter_des_item_2_title = lifetime_pack_starter + f"//div[2]//ul//li[2]"
    lifetime_pack_starter_des_item_3_icon = lifetime_pack_starter + f"//div[2]//ul//li[3]/i"
    lifetime_pack_starter_des_item_3_title = lifetime_pack_starter + f"//div[2]//ul//li[3]"

    lifetime_pack_starter_status = lifetime_pack_starter + f"div[3]//button"



class MyCloudText:
    title_text = "My Cloud"
    search_template = "A1"
    search_invalid_template = "Dummy Search is given, Expecting No Result."
    search_template_not_found_message = "You do not have any item with '" + search_invalid_template + "' in title"
    search_template_not_found_in_ws_message = "No files found in this WorkSpace."
    no_workspace_text = "You do not have any WorkSpace"
