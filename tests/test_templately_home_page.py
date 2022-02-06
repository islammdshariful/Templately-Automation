from src.site.home.home_page import HomePage
from src.site.mycloud.my_cloud import MyCloudDashboard
from src.site.signin.signin import SignIn
from src.site.signup.signup import SignUp
from utils.configuration import Config


def test_home_page(browser, cred):
    home_page = HomePage(browser)
    conf = Config(cred)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    home_page.load(conf.get_url('root'))
    home_page.check_homepage_content()


def test_create_account(browser, cred):
    conf = Config(cred)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    sign_up = SignUp(browser)
    sign_up.load(conf.get_url('signup'))
    sign_up.check_signup_page()
    # "first_name", "last_name", "email", "password", "con_password"
    sign_up.create_an_account("first_name", "last_name", "email", "password", "con_password")


def test_login_to_account(browser, cred):
    conf = Config(cred)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    sign_in = SignIn(browser, cred)
    sign_in.set_usr("user_1")
    # sign_in.load(conf.get_url('signin'))
    # sign_in.signin_through_page()
    sign_in.signin_through_modal()
    mc = MyCloudDashboard(browser)
    mc.signout()


def test_create_workspace(browser):
    mc = MyCloudDashboard(browser)
    mc.create_workspace()
    mc.edit_workspace()
    mc.delete_workspace('no')
