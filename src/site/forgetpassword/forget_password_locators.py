from selenium.webdriver.common.by import By


class ForgetPassLocators:
    # Modal
    modal_icon = f'/html/body/div[3]/div/div/div[1]'
    modal_title = (By.XPATH, f"//h4[@class='Modal_tly__modal__title__15D2K']")

    # Page
    icon = f'//*[@id="__next"]/div[3]/div/div/main/section/div/div/div[1]/div/div[1]'
    title = (By.XPATH, f"//h4[@class='Auth_tly__auth__title__1-i-h']")
    des = (By.XPATH, f"//h4[@class='Auth_tly__auth__body__title__1Jr1I']")

    email_field = (By.XPATH, f"//input[@id='reset-email']")

    reset_btn = (By.XPATH, f"//button[@class='Style_tly__button__26JVd Style_tly__primary__button__2oAmK']")

    sign_in_page = (By.XPATH, f"//a[@class='Style_tly__color__dark__3X6Ii']")

    success_msg = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/div[1]')

    toast_close_btn = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/button')


class ForgetPassText:
    modal_title_text = "Reset Password"
    title_text = "Forgot Password"
    success_msg_text = "Password reset link is sent in your email."
    des = "Recovery Email"
