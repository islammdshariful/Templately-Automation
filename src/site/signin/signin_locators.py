from selenium.webdriver.common.by import By


class SignInLocators:
    # Modal
    modal_icon = f'/html/body/div[3]/div/div/div[1]'
    modal_title = (By.XPATH, f"//h4[@class='Modal_tly__modal__title__15D2K']")
    modal_welcome_msg = (By.XPATH, f"//h4[@class='Modal_tly__modal__body__title__28cVN']")
    # Page
    icon = f'//*[@id="__next"]/div[3]/div/div/main/section/div/div/div[1]/div/div'
    title = (By.XPATH, f"//h4[@class='Auth_tly__auth__title__1-i-h']")
    welcome_msg = (By.XPATH, f"//h4[@class='Auth_tly__auth__body__title__1Jr1I']")

    email_field = (By.XPATH, f"//input[@id='username']")
    password_field = (By.XPATH, f"//input[@id='password']")

    sing_in_btn = (By.XPATH, f"//button[@class='Style_tly__button__26JVd Style_tly__primary__button__2oAmK']")

    new_here_label = (By.XPATH, f"//p[@class='Style_tly__color__secondary__2c7YL']")
    create_acc = (By.XPATH, f"//a[@class='Style_tly__color__dark__3X6Ii']")
    forget_pass = (By.XPATH, f"//a[normalize-space()='Forgot password?']")


class SignInText:
    sign_in_title_txt = "Sign In"
    welcome_ms_txt = "Great to have you back!"
    email_label_txt = "Email"
    password_label_txt = "Password"

    new_here_label_txt = "New here? Create a Templately account!"
    create_acc_txt = "Create a Templately account!"
    forget_pass_txt = "Forgot password?"

