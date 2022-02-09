from src.site.home.home_page import HomePage
from src.site.mycloud.my_cloud import MyWorkSpace, Dashboard, MyCloud
from src.site.signin.signin import SignIn
from src.site.signup.signup import SignUp
from utils.configuration import Configuration


def test_home_page(browser, read_credentials):
    home_page = HomePage(browser)
    conf = Configuration(read_credentials)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    home_page.load(conf.get_url('root'))
    home_page.check_homepage_content()


def test_create_account(browser, read_credentials):
    conf = Configuration(read_credentials)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    sign_up = SignUp(browser)
    sign_up.load(conf.get_url('signup'))
    sign_up.check_signup_page()
    # "first_name", "last_name", "email", "password", "con_password"
    sign_up.create_an_account("first_name", "last_name", "email", "password", "con_password")


def test_login_to_account_through_page(browser, read_credentials):
    conf = Configuration(read_credentials)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    sign_in = SignIn(browser, read_credentials)
    sign_in.set_usr("user_1")
    sign_in.signin_through_page(conf.get_url('signin'))
    d = Dashboard(browser)
    d.sign_out()


def test_login_to_account_through_modal(browser, read_credentials):
    conf = Configuration(read_credentials)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    sign_in = SignIn(browser, read_credentials)
    sign_in.set_usr("user_1")
    sign_in.signin_through_modal()
    d = Dashboard(browser)
    d.sign_out()


def test_my_workspace(browser):
    mc = MyWorkSpace(browser)
    mc.create_workspace()
    # mc.edit_workspace_outside_folder()
    # mc.edit_workspace_inside_folder()
    # mc.delete_workspace_outside_folder()
    # mc.delete_workspace_inside_folder()
    # mc.check_workspace()
    # mc.search_template_inside_workspace()


def test_my_cloud(browser):
    cl = MyCloud(browser)
    # cl.download_template('elementor')
    # cl.copy_to_workspace('elementor')
    # cl.move_to_workspace('elementor')
    # cl.delete_template('elementor')
    # cl.search_template()
    # cl.change_layout('layout')
