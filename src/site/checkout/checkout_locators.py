from selenium.webdriver.common.by import By


class CheckoutLocators:
    title = (By.XPATH, f"//h4[starts-with(@class, 'Auth_tly__auth__title')]")
    dropdown_btn = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__dropdown__toggler')]")
    item_premium_monthly = (By.XPATH, f"//ul[starts-with(@class, 'Style_tly__dropdown__menu__body')]//li[1]")
    item_premium_yearly = (By.XPATH, f"//ul[starts-with(@class, 'Style_tly__dropdown__menu__body')]//li[2]")
    item_premium_lifetime = (By.XPATH, f"//ul[starts-with(@class, 'Style_tly__dropdown__menu__body')]//li[3]")

    item_name = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__body')]//div[1]//div[1]//span")
    item_price = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__body')]//div[1]//div[2]//div//span")

    discount_label = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__body')]//div[2]//div[1]//span//span[2]")
    discount_label_icon = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__body')]//div[2]//div[1]//span//"
                                     f"span[1]//img")
    discount_percentage = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__body')]//div[2]//div[2]//div//span")

    total_label = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__body')]//div[3]//div[1]//span")
    total_ammount = (By.XPATH, f"//div[starts-with(@class, 'Table_tly__table__body')]//div[3]//div[2]//div//span")

    coupon_code_label = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__form__group')]//label")
    coupon_code_input = (By.XPATH, f"//input[@placeholder='XXXX-XXXX-XXXX-XXXX']")
    coupon_code_apply_btn = (By.XPATH, f"//button[normalize-space()='Apply']")

    pay_with_default_method = (By.XPATH, f"//label[normalize-space()='Pay With Default Method']")
    pay_with_other_option = (By.XPATH, f"//label[normalize-space()='Pay With Other Options']")
    choose_a_card_label = (By.XPATH, f"//h4[normalize-space()='Choose a Card']")

    terms_of_service = (By.XPATH, f"//input[@id='Privacy']")
    get_free_tips = (By.XPATH, f"//input[@id='condition']")

    pay_now_btn = (By.XPATH, f"//button[normalize-space()='Pay Now']")

    strip_icon = (By.XPATH, f"//i[@class='ticon t-shield']")
    checkout_protected_title = (By.XPATH, f"//p[starts-with(@class, 'Auth_tly__checkout__protected__title')]")
    checkout_protected_text = (By.XPATH, f"//small[starts-with(@class, 'Auth_tly__checkout__protected__text')]")

    benefit_header = (By.XPATH, f"//h4[normalize-space()='Benefits']")
    benefit_uws = (By.XPATH, f"//li[normalize-space()='Unlimited WorkSpace']")
    benefit_umc = (By.XPATH, f"//li[normalize-space()='Unlimited MyCloud items']")
    benefit_pi = (By.XPATH, f"//li[normalize-space()='Access to Pro Items']")

    # choose card
    choose_card = (By.XPATH, f"//div[starts-with(@class, 'Style_tly__payment__method__card__wrapper')]//div[1]//div[3]")

    # On Strip
    back_to_home = (By.XPATH, f"//img[@alt='Templately logo']")


