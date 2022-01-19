from selenium.webdriver.common.by import By


class SignUpLocators:
    icon = f"//*[name()='path' and @id='Path_382']"
    title = (By.XPATH, f"//h4[@class='Auth_tly__auth__title__1-i-h']")
    img = f"//img[@class='Grid_tly__w_100__ONLux']"

    fname_field = (By.XPATH, f"//input[@id='firstname']")
    lname_field = (By.XPATH, f"//input[@id='lastname']")
    email_field = (By.XPATH, f"//input[@id='primaryemail']")
    pass_field = (By.XPATH, f"//input[@id='password']")
    con_pass_field = (By.XPATH, f"//input[@id='confirmPass']")
    policy_field = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section/div/div/div[1]/div/div[2]/form/div[6]/'
                              f'div[1]/label/span/span')
    policy_page = (By.XPATH, f"//a[@class='Style_tly__color__primary__2HHZD'][normalize-space()='Privacy Policy']")
    terms_field = (By.XPATH, f'//*[@id="__next"]/div[3]/div/div/main/section/div/div/div[1]/div/div[2]/form/div[6]'
                             f'/div[2]/label/span/span')
    terms_page = (By.XPATH, f"//a[@class='Style_tly__color__primary__2HHZD'][normalize-space()='Terms of Services']")
    signin_page = (By.XPATH, f"//a[normalize-space()='Sign In']")
    signup_btn = (By.XPATH, f"//button[@class='Style_tly__button__26JVd Style_tly__primary__button__2oAmK']")

    success_msg = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/div[1]')
    toast_close_btn = (By.XPATH, f'/html/body/div[1]/div[1]/div/div/button')


class SignUpText:
    policy_label_text = "I Agree to the Templately Privacy Policy"
    terms_label_text = "I Agree to the Templately Terms of Services"
    signin_label_text = "Already have an account? Sign In"

    success_msg_text = "Account created successfully."
