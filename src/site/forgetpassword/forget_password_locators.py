from selenium.webdriver.common.by import By


class ForgetPassLocators:
    # Modal
    modal_icon = f"//div[starts-with(@class, 'Modal_tly__modal__head')]//*[name()='svg']"
    modal_title = (By.XPATH, f"//h4[normalize-space()='Reset Password']")

    # Page
    icon = f"//div[starts-with(@class, 'Auth_tly__auth__head')]//*[name()='svg']"
    title = (By.XPATH, f"//h4[normalize-space()='Forgot Password']")
    des = (By.XPATH, f"//h4[normalize-space()='Recovery Email']")

    email_field = (By.XPATH, f"//input[@id='reset-email']")

    reset_btn = (By.XPATH, f"//button[starts-with(@class, 'Style_tly__button')]")

    sign_in_page = (By.XPATH, f"//a[normalize-space()='Back to sign in']")
    sign_in_page_modal = (By.XPATH, f"//a[normalize-space()='Back to Sign In']")


class ForgetPassText:
    modal_title_text = "Reset Password"
    title_text = "Forgot Password"
    des = "Recovery Email"
