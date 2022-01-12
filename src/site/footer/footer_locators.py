from selenium.webdriver.common.by import By


class FooterLocators:
    # Footer
    footer_title = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/div[1]/div/img')
    footer_des = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/p[1]')
    social_fb = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[1]/a')
    social_tw = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[2]/a')
    social_in = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[3]/a')
    social_ins = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[4]/a')

    social_fb_icon = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[1]/a/i')
    social_tw_icon = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[2]/a/i')
    social_in_icon = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[3]/a/i')
    social_ins_icon = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/ul/li[4]/a/i')

    cr_label = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/p[2]')
    cr_com_link = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[1]/p[2]/a')

    com_label = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[1]/h5')
    com_about = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[1]/ul/li[1]/a')
    com_cont = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[1]/ul/li[2]/a')
    com_aff = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[1]/ul/li[3]/a')
    com_policy = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[1]/ul/li[4]/a')
    com_terms = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[1]/ul/li[5]/a')

    get_help_label = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[2]/h5')
    get_help_sup = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[2]/ul/li[1]/a')
    get_help_docs = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[2]/ul/li[2]/a')
    get_help_comm = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[2]/div[2]/div[2]/ul/li[3]/a')

    # Subscribe now
    subs_label = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[1]/div/div[1]/h3')
    subs_des = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[1]/div/div[1]/p')
    subs_email_field = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[1]/div/div[1]/form/div/input')
    subs_btn = (By.XPATH, f'//*[@id="__next"]/div[3]/footer/div[3]/div[1]/div/div[1]/form/div/button')
    subs_gif = (By.XPATH, f'//*[@id="eo0bfy6sj611"]')


class FooterTexts:
    footer_des_txt = "The Ultimate Templates Cloud for WordPress"
    social_fb_link = ""
    social_tw_link = ""
    social_in_link = ""
    social_ins_link = ""

    cr_label_txt = "© Copyright 2021. Powered by WPDeveloper"

    com_label_txt = "Company"
    com_about_txt = "About Us"
    com_cont_txt = "Contact"
    com_aff_txt = "Affiliate"
    com_policy_txt = "Privacy Policy"
    com_terms_txt = "Terms of Services"

    get_help_label_txt = "Get Help"
    get_help_sup_txt = "Support"
    get_help_docs_txt = "Docs"
    get_help_comm_txt = "Community"
