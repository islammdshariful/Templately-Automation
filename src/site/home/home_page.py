import time

from assertpy import soft_assertions, assert_that
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import *
from utils.config import *
from src.site.home.home_page_locators import HomePageLocators as loc
from src.site.home.home_page_locators import HomePageTexts as txt
from src.site.pack.pack_locators import PackLocators as ploc
from src.site.browse.browse_locators import BrowseLocators as bloc
from src.site.browse.browse_locators import BrowseText as btxt
from utils.helper import CheckText, CheckVisibility


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.c = CheckText(self.browser)
        self.d = CheckVisibility(self.browser)
        self.cursor = ActionChains(self.browser)

    def load(self):
        self.browser.get(BASEURL_site)

    def check_pricing(self, type):
        self.browser.execute_script("window.scrollTo(0, 8990)")
        time.sleep(1)
        assert_that(self.browser.find_element(*loc.license_unl_tem_label).text). \
            is_equal_to(txt.license_unl_tem_label_txt)
        assert_that(self.browser.find_element(*loc.license_unl_tem_des).text). \
            is_equal_to(txt.license_unl_tem_des_txt)

        # Starter
        if type == 'monthly':
            self.browser.find_element(*loc.monthly_toggle).click()
            time.sleep(1)
        else:
            self.browser.find_element(*loc.annual_toggle).click()
            time.sleep(1)

        assert_that(self.browser.find_element(*loc.mon_sta_label).text).is_equal_to(txt.mon_sta_label_txt)
        assert_that(self.browser.find_element(*loc.mon_sta_price).text).is_equal_to(txt.mon_sta_price_txt)
        assert_that(self.browser.find_element(*loc.mon_sta_disc_price).text).is_equal_to(txt.mon_sta_disc_price_txt)
        assert_that(self.browser.find_element(*loc.mon_sta_temp_items_label).text). \
            is_equal_to(txt.mon_sta_temp_items_label_txt)
        assert_that(self.browser.find_element(*loc.mon_sta_list_1).text).is_equal_to(txt.mon_sta_list_1_txt)
        assert_that(self.browser.find_element(*loc.mon_sta_list_2).text).is_equal_to(txt.mon_sta_list_2_txt)
        assert_that(self.browser.find_element(*loc.mon_sta_list_3).text).is_equal_to(txt.mon_sta_list_3_txt)
        if type == 'monthly':
            self.d.check_visibility(loc.mon_sta_icon, "Monthly starter icon not Visible")
            self.d.check_visibility(loc.mon_sta_list_1_icon, "Monthly starter List item 1 icon not Visible")
            self.d.check_visibility(loc.mon_sta_list_1_icon, "Monthly starter List item 2 icon not Visible")
            self.d.check_visibility(loc.mon_sta_list_1_icon, "Monthly starter List item 3 icon not Visible")
        else:
            self.d.check_visibility(loc.mon_sta_icon, "Annual starter icon not Visible")
            self.d.check_visibility(loc.mon_sta_list_1_icon, "Annual starter List item 1 icon not Visible")
            self.d.check_visibility(loc.mon_sta_list_1_icon, "Annual starter List item 2 icon not Visible")
            self.d.check_visibility(loc.mon_sta_list_1_icon, "Annual starter List item 3 icon not Visible")
        self.browser.find_element(*loc.mon_sta_temp_items).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*bloc.header).text).is_equal_to(btxt.header_txt)
        assert_that(self.browser.current_url).is_equal_to(BASEURL_site + "all?package=starter&page=1")
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 8990)")
        time.sleep(1)

        # Premium
        if type == 'annual':
            self.browser.find_element(*loc.annual_toggle).click()
            time.sleep(1)

        assert_that(self.browser.find_element(*loc.mon_prem_label).text).is_equal_to(txt.mon_prem_label_txt)
        if type == 'monthly':
            assert_that(self.browser.find_element(*loc.mon_prem_price).text).is_equal_to(txt.mon_prem_price_txt)
            assert_that(self.browser.find_element(*loc.mon_prem_disc_price).text). \
                is_equal_to(txt.mon_prem_disc_price_txt)
        else:
            assert_that(self.browser.find_element(*loc.ann_prem_price).text).is_equal_to(txt.ann_prem_price_txt)
            assert_that(self.browser.find_element(*loc.ann_prem_disc_price).text). \
                is_equal_to(txt.ann_prem_disc_price_txt)

        assert_that(self.browser.find_element(*loc.mon_prem_temp_items_label).text). \
            is_equal_to(txt.mon_prem_temp_items_label_txt)
        assert_that(self.browser.find_element(*loc.mon_prem_pro_temp_items_label).text). \
            is_equal_to(txt.mon_prem_pro_temp_items_label_txt)
        assert_that(self.browser.find_element(*loc.mon_prem_list_1).text).is_equal_to(txt.mon_prem_list_1_txt)
        assert_that(self.browser.find_element(*loc.mon_prem_list_2).text).is_equal_to(txt.mon_prem_list_2_txt)
        if type == 'monthly':
            self.d.check_visibility(loc.mon_sta_icon, "Monthly starter icon not Visible")
            self.d.check_visibility(loc.mon_prem_list_1_icon, "Monthly Premium List item 1 icon not Visible")
            self.d.check_visibility(loc.mon_prem_list_2_icon, "Monthly Premium List item 2 icon not Visible")
        else:
            self.d.check_visibility(loc.mon_sta_icon, "Annual starter icon not Visible")
            self.d.check_visibility(loc.mon_prem_list_1_icon, "Annual Premium List item 1 icon not Visible")
            self.d.check_visibility(loc.mon_prem_list_2_icon, "Annual Premium List item 2 icon not Visible")
        self.browser.find_element(*loc.mon_prem_temp_items).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*bloc.header).text).is_equal_to(btxt.header_txt)
        assert_that(self.browser.current_url).is_equal_to(BASEURL_site + "all?package=starter&page=1")
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 8990)")
        time.sleep(1)
        if type == 'annual':
            self.browser.find_element(*loc.annual_toggle).click()
            time.sleep(1)
        self.browser.find_element(*loc.mon_prem_pro_temp_items).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*bloc.header).text).is_equal_to(btxt.header_txt)
        assert_that(self.browser.current_url).is_equal_to(BASEURL_site + "all?package=pro&page=1")
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 8990)")
        time.sleep(1)

    def check_lifetime_pricing(self):
        self.browser.execute_script("window.scrollTo(0, 9676)")
        time.sleep(1)
        assert_that(self.browser.find_element(*loc.lftm_label).text).is_equal_to(txt.lftm_label_txt)
        assert_that(self.browser.find_element(*loc.lftm_price).text).is_equal_to(txt.lftm_price_txt)
        assert_that(self.browser.find_element(*loc.lftm_disc_price).text).is_equal_to(txt.lftm_disc_price_txt)
        assert_that(self.browser.find_element(*loc.lftm_temp_items_label).text). \
            is_equal_to(txt.lftm_temp_items_label_txt)
        assert_that(self.browser.find_element(*loc.lftm_pro_temp_items_label).text). \
            is_equal_to(txt.lftm_pro_temp_items_label_txt)
        assert_that(self.browser.find_element(*loc.lftm_des).text).is_equal_to(txt.lftm_des_txt)
        assert_that(self.browser.find_element(*loc.lftm_list_1).text).is_equal_to(txt.lftm_list_1_txt)
        assert_that(self.browser.find_element(*loc.lftm_list_2).text).is_equal_to(txt.lftm_list_2_txt)
        self.d.check_visibility(loc.lftm_icon, "Life Time icon not Visible")
        self.d.check_visibility(loc.lftm_list_1_icon, "Life Time List item 1 icon not Visible")
        self.d.check_visibility(loc.lftm_list_2_icon, "Life Time List item 2 icon not Visible")
        self.browser.find_element(*loc.lftm_temp_items).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*bloc.header).text).is_equal_to(btxt.header_txt)
        assert_that(self.browser.current_url).is_equal_to(BASEURL_site + "all?package=starter&page=1")
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 9676)")
        time.sleep(1)
        self.browser.find_element(*loc.lftm_pro_temp_items).click()
        time.sleep(1)
        assert_that(self.browser.find_element(*bloc.header).text).is_equal_to(btxt.header_txt)
        assert_that(self.browser.current_url).is_equal_to(BASEURL_site + "all?package=pro&page=1")
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 9676)")
        time.sleep(1)

    def home_page_header_content(self):
        self.c.check_title(txt.title_txt)
        assert_that(self.browser.find_element(*loc.header).text).is_equal_to(txt.header_txt)
        if self.browser.find_element(*loc.video).is_displayed():
            assert_that(display).is_equal_to(1)
            assert_that(self.browser.find_element(*loc.video_source).get_attribute('src')). \
                is_equal_to(txt.video_source_txt)
        else:
            assert_that(display).is_equal_to(" Header Video is not visible.")

        self.browser.find_element(*loc.how_it_works_btn).click()
        time.sleep(1)
        self.browser.find_element(*loc.how_it_works_close_btn).click()

    def home_page_could_workspace_content(self):
        assert_that(self.browser.find_element(*loc.cw_my_cloud_label).text).is_equal_to(txt.cw_my_cloud_label_txt)
        assert_that(self.browser.find_element(*loc.cw_my_cloud_des).text).is_equal_to(txt.cw_my_cloud_des_txt)
        assert_that(self.browser.find_element(*loc.cw_workspace_label).text).is_equal_to(txt.cw_workspace_label_txt)
        assert_that(self.browser.find_element(*loc.cw_workspace_des).text).is_equal_to(txt.cw_workspace_des_txt)

        self.browser.find_element(*loc.get_free_plugin_btn).click()
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[1])
        assert_that(self.browser.title).is_equal_to("Templately – Templates Cloud for Elementor & Gutenberg : "
                                                    "1000+ Free Designs! – WordPress plugin | WordPress.org")
        self.browser.close()
        self.browser.switch_to.window(windows[0])
        self.browser.execute_script("window.scrollTo(0, 1182)")
        time.sleep(1)
        self.browser.find_element(*loc.cw_how_it_works_btn).click()
        time.sleep(1)
        self.browser.find_element(*loc.cw_how_it_works_close_btn).click()

        if self.browser.find_element(*loc.cw_video).is_displayed():
            assert_that(display).is_equal_to(1)
            assert_that(self.browser.find_element(*loc.cw_video_source).get_attribute('src')). \
                is_equal_to(txt.cw_video_source_txt)
        else:
            assert_that(display).is_equal_to("Cloud Workspace Video is not visible.")

    def home_page_insight_content(self):
        self.browser.execute_script("window.scrollTo(0, 1182)")

        assert_that(self.browser.find_element(*loc.total_template_label).text). \
            is_equal_to(txt.total_template_label_txt)

        tt_count = self.browser.find_element(*loc.total_template).text
        if tt_count == "0":
            assert_that(display).is_equal_to("Total Template Count is Wrong")

        assert_that(self.browser.find_element(*loc.total_pack_label).text). \
            is_equal_to(txt.total_pack_label_txt)

        tp_count = self.browser.find_element(*loc.total_pack).text
        if tp_count == "0":
            assert_that(display).is_equal_to("Total Pack Count is Wrong")

        assert_that(self.browser.find_element(*loc.happy_users_label).text). \
            is_equal_to(txt.happy_users_label_txt)
        time.sleep(2)
        assert_that(self.browser.find_element(*loc.happy_users).text).is_equal_to(txt.happy_users_txt)

    def home_page_feature_items_content(self):
        self.browser.execute_script("window.scrollTo(0, 2186)")
        time.sleep(1)
        assert_that(self.browser.find_element(*loc.fi_label).text).is_equal_to(txt.fi_label_txt)

        fi_element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, loc.fi_item_title)))
        if self.browser.find_element(*loc.fi_item_img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Feature Items Image is not visible.")
        self.cursor.move_to_element(fi_element).perform()
        fi_item_title = fi_element.text
        fi_element.click()
        time.sleep(1)
        assert_that(self.browser.find_element(*ploc.title).text).is_equal_to(fi_item_title)
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 2186)")
        time.sleep(1)
        self.browser.find_element(*loc.fi_prev_btn).click()
        time.sleep(.5)
        self.browser.find_element(*loc.fi_nxt_btn).click()
        time.sleep(.5)

    def home_page_trending_items_content(self):
        self.browser.execute_script("window.scrollTo(0, 3451)")
        time.sleep(1)
        assert_that(self.browser.find_element(*loc.tre_items_label).text).is_equal_to(txt.tre_items_label_txt)
        tre_element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.XPATH, loc.tre_items_title)))
        if self.browser.find_element(*loc.tre_items_img).is_displayed():
            assert_that(display).is_equal_to(1)
        else:
            assert_that(display).is_equal_to("Trending Items Image is not visible.")
        self.cursor.move_to_element(tre_element).perform()
        tre_item_title = tre_element.text
        tre_element.click()
        time.sleep(1)
        assert_that(self.browser.find_element(*ploc.title).text).is_equal_to(tre_item_title)
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, 3451)")
        time.sleep(1)
        self.browser.find_element(*loc.tre_prev_btn).click()
        time.sleep(.5)
        self.browser.find_element(*loc.tre_nxt_btn).click()
        time.sleep(.5)

    def home_page_building_with_cloud_content(self):
        self.browser.execute_script("window.scrollTo(0, 7506)")
        time.sleep(1)
        assert_that(self.browser.find_element(*loc.bwc_the_feature_of_label).text). \
            is_equal_to(txt.bwc_the_feature_of_label_txt)
        assert_that(self.browser.find_element(*loc.bwc_building_with_cloud_label).text). \
            is_equal_to(txt.bwc_building_with_cloud_label_txt)

        item_1 = self.browser.find_element(*loc.bwc_item_1_title)
        self.cursor.move_to_element(item_1).perform()
        assert_that(item_1.text).is_equal_to(txt.bwc_item_1_title_txt)
        assert_that(self.browser.find_element(*loc.bwc_item_1_des).text).is_equal_to(txt.bwc_item_1_des_txt)

        item_2 = self.browser.find_element(*loc.bwc_item_2_title)
        self.cursor.move_to_element(item_2).perform()
        assert_that(item_2.text).is_equal_to(txt.bwc_item_2_title_txt)
        assert_that(self.browser.find_element(*loc.bwc_item_2_des).text).is_equal_to(txt.bwc_item_2_des_txt)

        item_3 = self.browser.find_element(*loc.bwc_item_3_title)
        self.cursor.move_to_element(item_3).perform()
        assert_that(item_3.text).is_equal_to(txt.bwc_item_3_title_txt)
        assert_that(self.browser.find_element(*loc.bwc_item_3_des).text).is_equal_to(txt.bwc_item_3_des_txt)

        item_4 = self.browser.find_element(*loc.bwc_item_4_title)
        self.cursor.move_to_element(item_4).perform()
        assert_that(item_4.text).is_equal_to(txt.bwc_item_4_title_txt)
        assert_that(self.browser.find_element(*loc.bwc_item_4_des).text).is_equal_to(txt.bwc_item_4_des_txt)

        item_5 = self.browser.find_element(*loc.bwc_item_5_title)
        self.cursor.move_to_element(item_5).perform()
        assert_that(item_5.text).is_equal_to(txt.bwc_item_5_title_txt)
        assert_that(self.browser.find_element(*loc.bwc_item_5_des).text).is_equal_to(txt.bwc_item_5_des_txt)

        item_6 = self.browser.find_element(*loc.bwc_item_6_title)
        self.cursor.move_to_element(item_6).perform()
        assert_that(item_6.text).is_equal_to(txt.bwc_item_6_title_txt)
        assert_that(self.browser.find_element(*loc.bwc_item_6_des).text).is_equal_to(txt.bwc_item_6_des_txt)

        self.d.check_visibility(loc.bwc_item_1_icon, "Build With Could Item 1 Icon not visible.")
        self.d.check_visibility(loc.bwc_item_2_icon, "Build With Could Item 2 Icon not visible.")
        self.d.check_visibility(loc.bwc_item_3_icon, "Build With Could Item 3 Icon not visible.")
        self.d.check_visibility(loc.bwc_item_4_icon, "Build With Could Item 4 Icon not visible.")
        self.d.check_visibility(loc.bwc_item_5_icon, "Build With Could Item 5 Icon not visible.")
        self.d.check_visibility(loc.bwc_item_6_icon, "Build With Could Item 6 Icon not visible.")

    def check_home_page_menus(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)

        # Pricing
        self.browser.find_element(*loc.menu_pricing).click()
        time.sleep(1)
        if self.browser.find_element(*loc.license_unl_tem_label).is_displayed():
            assert_that(display).is_equal_to(1)
            assert_that(self.browser.find_element(*loc.license_unl_tem_label).text). \
                is_equal_to(txt.license_unl_tem_label_txt)
            assert_that(self.browser.find_element(*loc.license_unl_tem_des).text). \
                is_equal_to(txt.license_unl_tem_des_txt)
        else:
            assert_that(display).is_equal_to("Pricing Menu not taking to the Pricing Content.")

        # Doc
        self.browser.find_element(*loc.menu_doc).click()
        time.sleep(1)
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[1])
        assert_that(self.browser.title).is_equal_to("Templately Documentations - Templately Documentations")
        self.browser.close()
        self.browser.switch_to.window(windows[0])

        # Blog
        self.browser.find_element(*loc.menu_blog).click()
        time.sleep(1)
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[1])
        assert_that(
            self.browser.find_element(By.XPATH,
            f'//*[@id="post-257982"]/div/div/div/div/section[1]/div[2]/div/div/div/div/div[1]/div/h2').text).\
            is_equal_to("Join our AWESOME Newsletter with 1 Million+ Users,\n"
                        "To do better in WordPress with Tips, Tricks & Deals!")
        self.browser.close()
        self.browser.switch_to.window(windows[0])

    def home_page_browse_wordpress_template(self):
        self.browser.execute_script("window.scrollTo(0, 4604)")
        assert_that(self.browser.find_element(*loc.wp_ready_to_import_label).text). \
            is_equal_to(txt.wp_ready_to_import_label_txt)
        assert_that(self.browser.find_element(*loc.wp_wordpress_template_label).text). \
            is_equal_to(txt.wp_wordpress_template_label_txt)
        self.browser.execute_script("window.scrollTo(0, 4857)")
        assert_that(self.browser.find_element(*loc.).text).is_equal_to(txt.)

    def testcase(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1)
        with soft_assertions():
            # Header
            self.home_page_header_content()

            # Could Workspace
            self.home_page_could_workspace_content()

            # Insight
            self.home_page_insight_content()

            # Feature Items
            self.home_page_feature_items_content()

            # Trending Items
            self.home_page_trending_items_content()

            # The Feature of Building With Cloud
            self.home_page_building_with_cloud_content()

            # 1 License. Unlimited Templates.
            # Monthly
            self.check_pricing('monthly')
            # Annual
            self.check_pricing('annual')
            # Life Time
            self.check_lifetime_pricing()

            # Menus
            self.check_home_page_menus()

            # Browse WordPress Templates
            self.home_page_browse_wordpress_template()
