from selenium.webdriver.common.by import By


class BrowseLocators:
    header = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/section/div[2]/div')


class AppliedFiltersLocators:
    filters = f"//div[starts-with(@class, 'AppliedFilter_tly__filter__result_wrapper')]"
    applied_filter_label = (By.XPATH, filters + f"//span[1]")
    applied_filter_1 = (By.XPATH, filters + f"//span[2]")
    applied_filter_1_remove = (By.XPATH, filters + f"//span[2]//button")
    applied_filter_2 = (By.XPATH, filters + f"//span[3]")
    applied_filter_2_remove = (By.XPATH, filters + f"//span[3]//button")
    applied_filter_3 = (By.XPATH, filters + f"//span[4]")
    applied_filter_3_remove = (By.XPATH, filters + f"//span[4]//button")
    applied_filter_4 = (By.XPATH, filters + f"//span[5]")
    applied_filter_4_remove = (By.XPATH, filters + f"//span[5]//button")
    applied_filter_5 = (By.XPATH, filters + f"//span[6]")
    applied_filter_5_remove = (By.XPATH, filters + f"//span[6]//button")

    clear_all_button = (By.XPATH, f"//button[normalize-space()='Clear All']")

    filter_by = f"//span[starts-with(@class,'AppliedFilter_tly__sort__items')]"
    platform_label = (By.XPATH, filter_by + f"//span[1]//span[1]")
    platform_dropdown = (By.XPATH, filter_by + f"//span[1]//span[2]//button")
    platform_dropdown_select_all = (By.XPATH, filter_by + f"//span[1]//span[2]//ui//li[1]")
    platform_dropdown_select_gutenberg = (By.XPATH, filter_by + f"//span[1]//span[2]//ui//li[2]")
    platform_dropdown_select_elementor = (By.XPATH, filter_by + f"//span[1]//span[2]//ui//li[3]")

    sort_label = (By.XPATH, filter_by + f"//span[2]//span[1]")
    sort_dropdown = (By.XPATH, filter_by + f"//span[2]//span[2]//button")
    sort_dropdown_select_select = (By.XPATH, filter_by + f"//span[2]//span[2]//ui//li[1]")
    sort_dropdown_select_most_popular = (By.XPATH, filter_by + f"//span[2]//span[2]//ui//li[2]")
    sort_dropdown_select_top_rating = (By.XPATH, filter_by + f"//span[2]//span[2]//ui//li[3]")
    sort_dropdown_select_latest_items = (By.XPATH, filter_by + f"//span[2]//span[2]//ui//li[4]")


class BrowserSearchSectionLocators:
    popular_search = f"//div[starts-with(@class, 'CommonSection_tly__filter__mixer')]"
    popular_search_1 = (By.XPATH, popular_search + f"//button[1]")
    popular_search_2 = (By.XPATH, popular_search + f"//button[2]")
    popular_search_3 = (By.XPATH, popular_search + f"//button[3]")
    popular_search_4 = (By.XPATH, popular_search + f"//button[4]")
    popular_search_5 = (By.XPATH, popular_search + f"//button[5]")
    popular_search_6 = (By.XPATH, popular_search + f"//button[6]")

    search_field = (By.XPATH, f"//input[@placeholder='Search here ...']")
    search_close_button = (By.XPATH, f"//button[starts-with(@class, 'Style_search_close_button')]")
    search_button = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__search__field__submit')]")


class Templates:
    pagination = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]")
    pagination_page_prev = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]//li[1]")
    pagination_page_next = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]//li[9]")
    pagination_page_2 = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]//li[3]")
    pagination_page_jump_to_next_from_page_1 = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]//li[7]")
    pagination_page_jump_to_prev = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]//li[3]")
    pagination_page_jump_to_next_from_page_6 = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]//li[9]")
    pagination_page_last = (By.XPATH, f"//div[starts-with(@class, 'Style_PaginationDiv')]//li[8]")

    templates = f"//div[starts-with(@class, 'ActiveFilter_tly__all__item__content')]//div[3]"
    template_1 = templates + f"//div[1]//div"
    template_1_slug_from_image = (By.XPATH, template_1 + f"//a[1]")
    template_1_slug_from_title = (By.XPATH, template_1 + f"//a[2]")
    template_1_name = (By.XPATH, template_1 + f"//a[2]//h4")
    template_1_ratings = (By.XPATH, template_1 + f"//div//div[1]")
    template_1_download = (By.XPATH, template_1 + f"//div//div[2]//span[2]")
    template_1_category = (By.XPATH, template_1 + f"//div//div[3]//span")
    template_1_type = (By.XPATH, template_1 + f"//a[1]//div[3]//div")

    template_9 = templates + f"//div[9]//div"
    template_9_slug_from_image = (By.XPATH, template_9 + f"//a[1]")
    template_9_slug_from_title = (By.XPATH, template_9 + f"//a[2]")
    template_9_name = (By.XPATH, template_9 + f"//a[2]//h4")
    template_9_ratings = (By.XPATH, template_9 + f"//div//div[1]")
    template_9_download = (By.XPATH, template_9 + f"//div//div[2]//span[2]")
    template_9_category = (By.XPATH, template_9 + f"//div//div[3]//span")
    template_9_type = (By.XPATH, template_9 + f"//a[1]//div[3]//div")


class BrowseText:
    header_txt = "READY TO IMPORT\nWordPress Templates"