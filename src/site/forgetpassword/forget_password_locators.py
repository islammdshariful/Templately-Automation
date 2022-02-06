from selenium.webdriver.common.by import By


class ForgetPassLocators:
    # Modal
    modal_icon = f'/html/body/div[3]/div/div/div[1]'
    modal_title = (By.XPATH, f"//h4[normalize-space()='Reset Password']")

    # Page
    icon = f'//*[@id="__next"]/div[3]/div/div/main/section/div/div/div[1]/div/div[1]'
    title = (By.XPATH, f"//h4[normalize-space()='Forgot Password']")
    des = (By.XPATH, f"//h4[normalize-space()='Recovery Email']")

    email_field = (By.XPATH, f"//input[@id='reset-email']")

    reset_btn = (By.XPATH, f"//button[@class='Style_tly__button__26JVd Style_tly__primary__button__2oAmK']")

    sign_in_page = (By.XPATH, f"//a[normalize-space()='Back to sign in']")
    sign_in_page_modal = (By.XPATH, f"//a[normalize-space()='Back to Sign In']")

    success_msg = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/div[1]')

    toast_close_btn = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/button')


class ForgetPassText:
    modal_title_text = "Reset Password"
    title_text = "Forgot Password"
    success_msg_text = "Password reset link is sent in your email."
    des = "Recovery Email"
