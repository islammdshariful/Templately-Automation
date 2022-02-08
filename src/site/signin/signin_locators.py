from selenium.webdriver.common.by import By


class SignInLocators:
    # Modal
    modal_icon = f"//div[starts-with(@class, 'Modal_tly__modal__head')]//*[name()='svg']"
    modal_title = (By.XPATH, f"//h4[normalize-space()='Sign In']")
    modal_welcome_msg = (By.XPATH, f"//h4[normalize-space()='Great to have you back!']")
    # Page
    icon = f"//div[starts-with(@class, 'Auth_tly__auth__head')]//*[name()='svg']"
    title = (By.XPATH, f"//h4[normalize-space()='Sign In']")
    welcome_msg = (By.XPATH, f"//h4[normalize-space()='Great to have you back!']")

    email_field = (By.XPATH, f"//input[@id='username']")
    password_field = (By.XPATH, f"//input[@id='password']")

    sing_in_btn = (By.XPATH, f"//button[normalize-space()='Sign in']")

    new_here_label = (By.XPATH, f"//p[starts-with(@class, 'Style_tly__color__secondary')]")
    create_acc = (By.XPATH, f"//a[normalize-space()='Create a Templately account!']")
    forget_pass = (By.XPATH, f"//a[normalize-space()='Forgot password?']")


class SignInText:
    sign_in_title_txt = "Sign In"
    welcome_ms_txt = "Great to have you back!"
    email_label_txt = "Email"
    password_label_txt = "Password"

    new_here_label_txt = "New here? Create a Templately account!"
    create_acc_txt = "Create a Templately account!"
    forget_pass_txt = "Forgot password?"

