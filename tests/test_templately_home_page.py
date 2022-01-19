from src.site.home.home_page import HomePage
from src.site.signin.signin import SignIn
# from src.site.signup.signup import SignUp
from src.site.signup.signup import SignUp
from utils.configuration import Config
from utils.set_users import User


def test_home_page(browser):
    home_page = HomePage(browser)
    conf = Config()
    conf.set_env('live')
    home_page.load(conf.get_url('root'))
    home_page.testcase()


def test_create_account(browser):
    conf = Config()
    conf.set_env('live')
    sign_up = SignUp(browser)
    sign_up.load(conf.get_url('signup'))
    sign_up.testcase()
    sign_up.create_an_account("first_name", "last_name", "email", "password", "con_password")


def test_login_to_account(browser, config):
    conf = Config()
    conf.set_env('live')
    sign_in = SignIn(browser, config)
    sign_in.set_usr("user_1")
    sign_in.load(conf.get_url('signin'))
    sign_in.testcase()
