from selenium.webdriver.common.by import By


class HomePageLocators:
    # Menu
    menu_home = (By.XPATH, f"//a[normalize-space()='Home']")
    menu_browse = (By.XPATH, f"//a[normalize-space()='Browse']")
    menu_pricing = (By.XPATH, f"//a[normalize-space()='Pricing']")
    menu_doc = (By.XPATH, f"//a[normalize-space()='Doc']")
    menu_blog = (By.XPATH, f"//a[normalize-space()='Blog']")

    my_cloud_btn = (By.XPATH, f"//a[starts-with(@class, 'Style_tly__button')]")
    signin_btn = (By.XPATH, "//button[normalize-space()='Sign In']")

    # Header
    header = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/div/section/div[3]/div/div/div[1]/h1')
    video = f'//*[@id="__next"]/div[2]/div/div/main/div/section/div[3]/div/div/div[2]/div/div/video'
    video_source = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/div/section/div[3]/div/div/div[2]/div/div'
                              f'/video/source')
    get_started_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/div/section/div[3]/div/div/div[1]/div/a/span')

    how_it_works_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/div/section/div[3]/div/div/div[1]/div'
                                  f'/button/span[2]')

    how_it_works_close_btn = (By.XPATH, f'/html/body/div[5]/div/div/div[1]/span')

    # Insight
    total_template = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[1]/div[2]/div/div/div/div[1]/div'
                                f'/div[2]/h4/div')
    total_template_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[1]/div[2]/div/div/div/div[1]'
                                      f'/div/div[2]/p')

    total_pack = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[1]/div[2]/div/div/div/div[2]/div/div[2]'
                            f'/h4/div')
    total_pack_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[1]/div[2]/div/div/div/div[2]/div'
                                  f'/div[2]/p')

    happy_users = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[1]/div[2]/div/div/div/div[3]/div/div[2]'
                             f'/h4/div')
    happy_users_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[1]/div[2]/div/div/div/div[3]/div'
                                   f'/div[2]/p')

    # Could Wordspace
    cw_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[2]/div[1]/h3')
    cw_my_cloud_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[2]/h4[1]')
    cw_my_cloud_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[2]/p[1]')

    cw_workspace_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[2]/h4[2]')
    cw_workspace_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[2]/p[2]')
    get_free_plugin_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[2]/div[2]/a/span')
    cw_how_it_works_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[2]/div[2]/button'
                                     f'/span[2]')
    cw_how_it_works_close_btn = (By.XPATH, f'/html/body/div[6]/div/div/div[1]/span')
    cw_video = f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[1]/div/div/video'
    cw_video_source = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[2]/div/div/div[1]/div/div/video'
                                 f'/source')

    # Feature Items
    fi_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[3]/div[3]/div[1]/h3')
    fi_item_title = f'//*[@id="__next"]/div[2]/div/div/main/section[3]/div[3]/div[2]/div/div/ul/li[7]/div/a/div/h4'
    fi_item_img = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[3]/div[3]/div[2]/div/div/ul/li[7]'
                             f'/div/a/div/span/img')
    fi_prev_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[3]/div[3]/div[2]/div/div/button[1]')
    fi_nxt_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[3]/div[3]/div[2]/div/div/button[2]')

    # Trending Items
    tre_items_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[4]/div[2]/div[1]/h3')
    tre_items_img = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[4]/div[2]/div[2]/div/div/ul/li[5]/'
                               f'div/a/div[2]/span/img')
    tre_items_title = f'//*[@id="__next"]/div[2]/div/div/main/section[4]/div[2]/div[2]/div/div/ul/li[5]/div/a/div[2]/h4'
    tre_prev_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[4]/div[2]/div[2]/div/div/button[1]')
    tre_nxt_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[4]/div[2]/div[2]/div/div/button[2]')

    # WordPress Templates
    wp_ready_to_import_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[2]/div/h4')
    wp_wordpress_template_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[2]/div/h3')

    wp_filter_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[1]/h6')
    wp_filter_menu_hide = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[1]'
                                     f'/button/i')
    wp_filter_menu_show = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/button')
    # Filter
    wp_filter_all = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]/div[1]'
                               f'/button[1]')
    wp_filter_starter = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]'
                                   f'/div[1]/button[2]')
    wp_filter_pro = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]/div[1]'
                               f'/button[3]')
    # Top filter
    wp_applied_filter_top_result_1 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                f'/div[2]/div[2]/div/div/span[2]/span')
    wp_applied_filter_top_result_1_cancel_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]'
                                                           f'/div/div/div[2]/div[2]/div/div/span[2]/button')

    # Filter By Blocks
    wp_filter_blocks_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]'
                                        f'/div[2]/div[1]/div[1]/h5')
    wp_filter_blocks_all_blocks = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                             f'/div[2]/div[2]/div[1]/div[2]/ul/li[1]/button')
    wp_filter_blocks_blocks = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                         f'/div[2]/div[2]/div[1]/div[2]/ul/li[2]/button')
    wp_filter_blocks_faq = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                      f'/div[2]/div[2]/div[1]/div[2]/ul/li[3]/button')
    wp_filter_blocks_footer = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                         f'/div[2]/div[2]/div[1]/div[2]/ul/li[4]/button')
    wp_filter_blocks_gutenberg = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                            f'/div[2]/div[2]/div[1]/div[2]/ul/li[5]/button')
    wp_filter_blocks_hero = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                       f'/div[2]/div[2]/div[1]/div[2]/ul/li[6]/button')
    # Filter By Pages
    wp_filter_pages_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]'
                                       f'/div[2]/div[2]/div[1]/h5')
    wp_filter_pages_all_pages = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                           f'/div[2]/div[2]/div[2]/div[2]/ul/li[1]/button')
    wp_filter_pages_archive = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                         f'/div[2]/div[2]/div[2]/div[2]/ul/li[2]/button')
    wp_filter_pages_footer = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                        f'/div[2]/div[2]/div[2]/div[2]/ul/li[3]/button')
    wp_filter_pages_landing_page = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                              f'/div[2]/div[2]/div[2]/div[2]/ul/li[4]/button')
    wp_filter_pages_product_archive = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                 f'/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[5]/button')
    wp_filter_pages_single_page = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                             f'/div[2]/div[2]/div[2]/div[2]/ul/li[6]/button')
    wp_filter_pages_single_post = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                             f'/div[2]/div[2]/div[2]/div[2]/ul/li[7]/button')
    wp_filter_pages_single_product = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/'
                                                f'div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[8]/button')
    # Filter By Packs
    wp_filter_packs_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]'
                                       f'/div[2]/div[3]/div[1]/h5')
    wp_filter_packs_all_packs = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                           f'/div[2]/div[2]/div[3]/div[2]/ul/li[1]/button')
    wp_filter_packs_landing_page = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                              f'/div[2]/div[2]/div[3]/div[2]/ul/li[2]/button')
    wp_filter_packs_single_page = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                             f'/div[2]/div[2]/div[3]/div[2]/ul/li[3]/button')
    wp_filter_packs_site_template = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                               f'/div[2]/div[2]/div[3]/div[2]/ul/li[4]/button')
    # Filter By Tags
    wp_filter_tags_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]'
                                      f'/div[3]/div[1]/h5')
    wp_filter_tags_search_feild = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                             f'/div[2]/div[3]/div[1]/div[1]/input')
    wp_filter_tags_visibility_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                               f'/div[1]/div[2]/div[3]/div[1]/div[2]/i')
    wp_filter_tags_see_more_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                             f'/div[2]/div[3]/div[2]/div[2]/button[1]')
    wp_filter_tags_apply_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                          f'/div[2]/div[3]/div[2]/div[2]/button[2]')
    wp_filter_tags_list_1 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]'
                                       f'/div[3]/div[2]/div[1]/label[1]')
    wp_filter_tags_list_2 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]/div[2]'
                                       f'/div[3]/div[2]/div[1]/label[2]')
    # Filter By Dependency
    wp_filter_dependency_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[1]'
                                            f'/div[2]/div[4]/div[1]/h5')
    wp_filter_dependency_visibility_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                     f'/div[1]/div[2]/div[4]/div[1]/div/i')
    wp_filter_dependency_see_more_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                   f'/div[1]/div[2]/div[4]/div[2]/div[2]/button[1]')
    wp_filter_dependency_apply_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                f'/div[1]/div[2]/div[4]/div[2]/div[2]/button[2]')
    wp_filter_dependency_list_1_icon = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                  f'/div[1]/div[2]/div[4]/div[2]/div[1]/button[1]/span[1]/div/img')
    wp_filter_dependency_list_1_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                   f'/div[1]/div[2]/div[4]/div[2]/div[1]/button[1]/span[2]')
    wp_filter_dependency_list_2_icon = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                  f'/div[1]/div[2]/div[4]/div[2]/div[1]/button[2]/span[1]/div/img')
    wp_filter_dependency_list_2_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                   f'/div[1]/div[2]/div[4]/div[2]/div[1]/button[2]/span[2]')
    # Search Top Bar
    wp_search_field = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[1]'
                                 f'/div[2]/div[1]/div/div/input')
    wp_search_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[1]'
                               f'/div[2]/div[1]/div/button')
    wp_search_popular_keys_1 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                          f'/div[1]/div[2]/div[2]/button[1]')
    wp_search_popular_keys_2 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                          f'/div[1]/div[2]/div[2]/button[2]')
    wp_search_popular_keys_3 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                          f'/div[1]/div[2]/div[2]/button[3]')
    wp_search_popular_keys_4 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                          f'/div[1]/div[2]/div[2]/button[4]')
    wp_search_popular_keys_5 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                          f'/div[1]/div[2]/div[2]/button[5]')
    wp_search_popular_keys_6 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                          f'/div[1]/div[2]/div[2]/button[6]')
    wp_search_popular_keys_7 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                          f'/div[1]/div[2]/div[2]/button[7]')
    # Search Filtered Result
    wp_applied_filter_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                         f'/div[2]/span[1]')
    # Popular
    wp_applied_filter_popular_result_1 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div'
                                                    f'/div/div[2]/div[2]/div/span[1]')
    wp_applied_filter_popular_result_1_cancel_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]'
                                                               f'/div[3]/div/div/div[2]/div[2]/div/span[1]/button/i')
    wp_applied_filter_popular_result_2 = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                                    f'/div[2]/div[2]/div/span[2]')
    wp_applied_filter_popular_result_2_cancel_btn = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]'
                                                               f'/div[3]/div/div/div[2]/div[2]/div/span[2]/button/i')
    wp_applied_filter_clear_all_btn = (By.XPATH, f"//button[normalize-space()='Clear All']")

    # Search Filter Result Sort
    wp_applied_filter_sort_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]'
                                              f'/div[2]/span[2]/span[1]')
    wp_applied_filter_sort_select = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div'
                                               f'/div[2]/div[2]/span[2]/span[2]/button')
    wp_applied_filter_sort_select_select = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]'
                                                      f'/div/div/div[2]/div[2]/span[2]/span[2]/ul/li[1]')
    wp_applied_filter_sort_select_most_popular = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]'
                                                            f'/div/div/div[2]/div[2]/span[2]/span[2]/ul/li[2]')
    wp_applied_filter_sort_select_top_ratings = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]'
                                                           f'/div/div/div[2]/div[2]/span[2]/span[2]/ul/li[3]')
    wp_applied_filter_sort_select_latest = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]'
                                                      f'/div/div/div[2]/div[2]/span[2]/span[2]/ul/li[4]')

    # Template information - 1
    wp_template_1_title = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[1]/div' \
                          f'/div/a[2]/h4'
    wp_template_1_ratings_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]' \
                                 f'/div[1]/div/div/div/div[1]/button/span[1]/i'
    wp_template_1_ratings = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[1]' \
                            f'/div/div/div/div[1]/button/span[2]'
    wp_template_1_download_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]' \
                                  f'/div[1]/div/div/div/div[2]/span[1]/i'
    wp_template_1_download = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[1]' \
                             f'/div/div/div/div[2]/span[2]'
    wp_template_1_category = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[1]' \
                             f'/div/div/div/div[3]/span'
    wp_template_1_category_on_img = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]' \
                                    f'/div[1]/div/div/a[1]/div[3]/div'

    # Template information - 2
    wp_template_2_title = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[9]' \
                          f'/div/div/a[2]/h4'
    wp_template_2_ratings_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]' \
                                 f'/div[9]/div/div/div/div[1]/button/span[1]/i'
    wp_template_2_ratings = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[9]' \
                            f'/div/div/div/div[1]/button/span[2]'
    wp_template_2_download_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]' \
                                  f'/div[9]/div/div/div/div[2]/span[1]/i'
    wp_template_2_download = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[9]' \
                             f'/div/div/div/div[2]/span[2]'
    wp_template_2_category = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]/div[9]' \
                             f'/div/div/div/div[3]/span'
    wp_template_2_category_on_img = f'//*[@id="__next"]/div[2]/div/div/main/section[5]/div[3]/div/div/div[2]/div[3]' \
                                    f'/div[9]/div/div/a[1]/div[3]/div'

    # Building With Cloud
    bwc_the_feature_of_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[1]/h4')
    bwc_building_with_cloud_label = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[1]/h3')

    bwc_item_1_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[1]/div/div/object'
    bwc_item_1_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[1]/div/h4')
    bwc_item_1_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[1]/div/p')
    bwc_item_2_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[2]/div/div/object'
    bwc_item_2_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[2]/div/h4')
    bwc_item_2_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[2]/div/p')
    bwc_item_3_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[3]/div/div/object'
    bwc_item_3_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[3]/div/h4')
    bwc_item_3_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[3]/div/p')
    bwc_item_4_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[4]/div/div/object'
    bwc_item_4_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[4]/div/h4')
    bwc_item_4_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[4]/div/p')
    bwc_item_5_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[5]/div/div/object'
    bwc_item_5_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[5]/div/h4')
    bwc_item_5_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[5]/div/p')
    bwc_item_6_icon = f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[6]/div/div/object'
    bwc_item_6_title = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[6]/div/h4')
    bwc_item_6_des = (By.XPATH, f'//*[@id="__next"]/div[2]/div/div/main/section[6]/div[3]/div[2]/div[6]/div/p')

    # License
    license_unl_tem_label = (By.XPATH, f'//*[@id="pricing"]/div/div[1]/h2[1]')
    license_unl_tem_des = (By.XPATH, f'//*[@id="pricing"]/div/div[1]/h2[2]')

    monthly_toggle = (By.XPATH, f'//*[@id="pricing"]/div/div[2]/div/button[1]')
    annual_toggle = (By.XPATH, f'//*[@id="pricing"]/div/div[2]/div/button[2]')

    mon_sta_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[2]/div[2]/h5')
    mon_sta_icon = f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[2]/div[1]/i'
    mon_sta_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[2]/div[2]/p/del')
    mon_sta_disc_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[2]/div[2]/p/span')
    mon_sta_temp_items = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/p/a')
    mon_sta_temp_items_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/p')
    mon_sta_list_1 = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/ul/li[1]')
    mon_sta_list_1_icon = f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/ul/li[1]/i'
    mon_sta_list_2 = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/ul/li[2]')
    mon_sta_list_2_icon = f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/ul/li[2]/i'
    mon_sta_list_3 = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/ul/li[3]')
    mon_sta_list_3_icon = f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[3]/ul/li[3]/i'
    mon_sta_get_started_btn = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[1]/div/div[4]/a/span')

    mon_prem_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[2]/div[2]/h5')
    mon_prem_icon = f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[2]/div[1]/i'
    mon_prem_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[2]/div[2]/p/del')
    mon_prem_disc_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[2]/div[2]/p/span')
    mon_prem_temp_items = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/p[1]/a')
    mon_prem_temp_items_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/p[1]')
    mon_prem_pro_temp_items = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/p[2]/a')
    mon_prem_pro_temp_items_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/p[2]')
    mon_prem_list_1 = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/ul/li[1]')
    mon_prem_list_1_icon = f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/ul/li[1]/i'
    mon_prem_list_2 = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/ul/li[2]')
    mon_prem_list_2_icon = f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[3]/ul/li[2]/i'
    mon_prem_get_started_btn = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[4]/a')

    ann_prem_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[2]/div[2]/p/del')
    ann_prem_disc_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[2]/div/div[2]/div[2]/p/span')

    lftm_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[1]/div[2]/h5')
    lftm_icon = f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[1]/div[1]/i'
    lftm_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[1]/div[2]/p/del')
    lftm_disc_price = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[1]/div[2]/p/span')
    lftm_temp_items = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/p[1]/a')
    lftm_temp_items_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/p[1]')
    lftm_pro_temp_items = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/p[2]/a')
    lftm_pro_temp_items_label = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/p[2]')
    lftm_list_1 = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/ul/li[1]')
    lftm_list_1_icon = f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/ul/li[1]/i'
    lftm_list_2 = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/ul/li[2]')
    lftm_list_2_icon = f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[2]/ul/li[2]/i'
    lftm_get_started_btn = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[1]/div[2]/div/a/span')
    lftm_des = (By.XPATH, f'//*[@id="pricing"]/div/div[3]/div[3]/div/div[1]/div[2]/small')


class HomePageTexts:
    # Header
    title_txt = 'Templately - The Best Elementor Templates for WordPress & Cloud WorkSpace for 2022'
    video_source_txt = "https://assets.templately.com/frontend/Landing%20Page%20Intro%20V2.0.mp4"
    header_txt = "Ultimate\nTEMPLATES\nCloud for WordPress"

    # Insight
    total_template_label_txt = "TOTAL TEMPLATES"
    total_pack_label_txt = "TOTAL PACKS"
    happy_users_label_txt = "HAPPY USERS"
    happy_users_txt = "200,000+"

    # Could Wordspace
    cw_label_txt = "Cloud Workspace"
    cw_my_cloud_label_txt = "My Cloud"
    cw_my_cloud_des_txt = "Save & store your page templates on MyCloud to reuse it whenever you need"

    cw_workspace_label_txt = "WorkSpace"
    cw_workspace_des_txt = "Invite your team members & work together to build website faster than ever before"
    cw_video_source_txt = "https://assets.templately.com/frontend/Cloud%20IntroV2.mp4"

    # Feature Items
    fi_label_txt = "Featured Items"

    # Trending Items
    tre_items_label_txt = "Trending Items"

    # WordPress Templates
    wp_ready_to_import_label_txt = "READY TO IMPORT"
    wp_wordpress_template_label_txt = "WordPress Templates"
    wp_filter_label_txt = "Filter & Refine"

    # Filter By Blocks
    wp_filter_blocks_label_txt = "Pages"
    # Filter By Pages

    # Filter By Packs
    wp_filter_packs_label_txt = "Packs"

    # Filter By Tags
    wp_filter_tags_label_txt = "Tags"

    # Filter By Dependency
    wp_filter_dependency_label_txt = "Dependency"

    # Search Filtered Result
    wp_applied_filter_label_txt = "Applied Filters :"

    wp_applied_filter_clear_all_btn_txt = "Clear All"

    # Search Filter Result Sort
    wp_applied_filter_sort_label_txt = "Sort :"
    wp_applied_filter_sort_select_select_txt = "Select"
    wp_applied_filter_sort_select_most_popular_txt = "Most Popular"
    wp_applied_filter_sort_select_top_ratings_txt = "Top Rating"
    wp_applied_filter_sort_select_latest_txt = "Latest"

    # Building With Cloud
    bwc_the_feature_of_label_txt = "THE FEATURE OF"
    bwc_building_with_cloud_label_txt = "Building With Cloud"

    bwc_item_1_title_txt = "Stunning Starter Templates"
    bwc_item_1_des_txt = "Sign up right now and get started with beautiful Templates"
    bwc_item_2_title_txt = "Seamless Integration With Page Builders"
    bwc_item_2_des_txt = "Create landing pages with Elementor, Gutenberg and more"
    bwc_item_3_title_txt = "Advanced Premium Templates"
    bwc_item_3_des_txt = "Create conversion optimized landing pages for every niche"
    bwc_item_4_title_txt = "Download WordPress Plugin"
    bwc_item_4_des_txt = "Install WordPress Plugin & start importing templates right now"
    bwc_item_5_title_txt = "Free Storage at MyCloud"
    bwc_item_5_des_txt = "Access all your Saved Templates anytime from any device"
    bwc_item_6_title_txt = "Dedicated Support Team"
    bwc_item_6_des_txt = "Get immediate assistance from our super friendly support"

    # License
    license_unl_tem_label_txt = "1 License. Unlimited Templates."
    license_unl_tem_des_txt = "Join With 100,000+ Users & Power Up Your Entire Team To Build Websites Faster"

    mon_sta_label_txt = "STARTER"
    mon_sta_price_txt = "$9.99"
    mon_sta_disc_price_txt = "$0"
    mon_sta_temp_items_label_txt = "1084 STARTER\nItems"
    mon_sta_list_1_txt = "My Cloud 100 Items"
    mon_sta_list_2_txt = "No Pro Item"
    mon_sta_list_3_txt = "1 WorkSpace"

    mon_prem_label_txt = "PREMIUM"
    mon_prem_price_txt = "$19.99"
    mon_prem_disc_price_txt = "$6.99"
    mon_prem_temp_items_label_txt = "1084 STARTER\nItems"
    mon_prem_pro_temp_items_label_txt = "732 PRO\nItems"
    mon_prem_list_1_txt = "My Cloud Unlimited Items"
    mon_prem_list_2_txt = "Unlimited WorkSpace"
    mon_prem_discount_label = "Special discount 2021"
    mon_prem_discount_percentage = "-30%"

    ann_prem_price_txt = "$199.99"
    ann_prem_disc_price_txt = "$59.99"
    ann_prem_discount_label = "Get Started 2021"
    ann_prem_discount_percentage = "-40%"

    lftm_label_txt = "LIFETIME"
    lftm_price_txt = "$999.99"
    lftm_disc_price_txt = "$299.99"
    lftm_temp_items_label_txt = "1084 STARTER\nItems"
    lftm_pro_temp_items_label_txt = "732 PRO\nItems"
    lftm_list_1_txt = "My Cloud Unlimited Items"
    lftm_list_2_txt = "Unlimited WorkSpace"
    lftm_des_txt = "Pay Once, Use Forever"
    lftm_prem_discount_label = "Get Started Lifetime"
    lftm_prem_discount_percentage = "-70%"
