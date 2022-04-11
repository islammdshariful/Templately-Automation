from src.site.checkout.checkout import Checkout
from src.site.dashboard.dashboard import Dashboard
from src.site.dashboard.manage_api import ManageAPI
from src.site.dashboard.my_workspace import MyWorkSpace
from src.site.dashboard.subscription import Subscription
from src.site.home.home_page import HomePage
from src.site.dashboard.my_cloud import MyCloud
from src.site.dashboard.profile import Profile
from src.site.signin.signin import SignIn
from src.site.signup.signup import SignUp
from utils.configuration import Configuration
from datetime import datetime


def test_login_to_account_through_page(browser, read_credentials):
    conf = Configuration(read_credentials)
    conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
    sign_in = SignIn(browser, read_credentials)
    sign_in.set_usr("user_1")
    sign_in.signin_through_page(conf.get_url('signin'))
    # d = Dashboard(browser)
    # d.sign_out()


def test_create_workspace(browser):
    mc = MyWorkSpace(browser)
    mc.create_workspace('testerbhaai@gmail.com')


def test_manage_my_cloud_with_elementor(browser):
    cl = MyCloud(browser)
    cl.download_template('elementor')
    cl.copy_to_workspace('elementor')
    cl.move_to_workspace('elementor')
    # cl.delete_template('elementor')


def test_manage_my_cloud_with_gutenberg(browser):
    cl = MyCloud(browser)
    cl.download_template('gutenberg')
    cl.copy_to_workspace('gutenberg')
    cl.move_to_workspace('gutenberg')
    # cl.delete_template('gutenberg')


def test_search_template(browser):
    cl = MyCloud(browser)
    cl.search_template("A2")
    cl.change_layout('layout')


def test_update_profile_information(browser, read_credentials):
    p = Profile(browser, read_credentials)
    now = datetime.now()
    name = now.strftime("%A")
    p.change_personal_info("Mr.", name)
    p.update_email('testerbhaai+1@gmail.com')


def test_update_account_password(browser, read_credentials):
    p = Profile(browser, read_credentials)
    p.set_usr('user_1')
    p.change_password('user_1', '123AbC456new')


def test_payment_method(browser, read_credentials):
    p = Profile(browser, read_credentials)
    p.set_env('live')
    p.payment_method('5555 5555 5555 4444')
    p.payment_method_remove_delete_card()


# def test_check_my_favorites(browser, read_credentials):
#     p = Profile(browser, read_credentials)
#     p.my_favorites('starter', 'block')


def test_check_my_downloads(browser, read_credentials):
    p = Profile(browser, read_credentials)
    p.my_downloads()


def test_manage_api(browser):
    api = ManageAPI(browser)
    api.create_token()
    api.copy_token()
    api.delete_token()
