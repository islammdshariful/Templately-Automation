from src.site.browse.browser import BrowseTemplates
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


# def test_home_page(browser, read_credentials):
#     home_page = HomePage(browser)
#     conf = Configuration(read_credentials)
#     conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
#     home_page.load(conf.get_url('root'))
#     home_page.check_homepage_content()
#
#
# def test_create_account(browser, read_credentials):
#     conf = Configuration(read_credentials)
#     conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
#     sign_up = SignUp(browser)
#     sign_up.load(conf.get_url('signup'))
#     sign_up.check_signup_page()
#     # "first_name", "last_name", "email", "password", "con_password"
#     sign_up.create_an_account("first_name", "last_name", "email", "password", "con_password")
#
#
# def test_login_to_account_through_page(browser, read_credentials):
#     conf = Configuration(read_credentials)
#     conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
#     sign_in = SignIn(browser, read_credentials)
#     sign_in.set_usr("user_1")
#     sign_in.signin_through_page(conf.get_url('signin'))
#     d = Dashboard(browser)
#     d.sign_out()
#
#
# def test_login_to_account_through_modal(browser, read_credentials):
#     conf = Configuration(read_credentials)
#     conf.set_env('live')  # For Live → 'live' For Dev → 'dev'
#     sign_in = SignIn(browser, read_credentials)
#     sign_in.set_usr("user_1")
#     sign_in.signin_through_modal()
#     d = Dashboard(browser)
#     d.sign_out()
#
#
# def test_my_workspace(browser):
#     mc = MyWorkSpace(browser)
#     mc.create_workspace('testerbhaai@gmail.com')
#     mc.edit_workspace_outside_folder()
#     mc.edit_workspace_inside_folder()
#     mc.delete_workspace_outside_folder('no')
#     mc.create_workspace('testerbhaai@gmail.com')
#     mc.delete_workspace_inside_folder('no')
#     mc.check_workspace()
#     mc.search_template_inside_workspace()
#     mc.add_template_to_workspace('my_cloud')
#     mc.share_workspace_outside_folder('testerbhaai+1@gmail.com')
#     mc.share_workspace_inside_folder('testerbhaai+1@gmail.com')
#
#
# def test_my_cloud(browser):
#     cl = MyCloud(browser)
#     # cl.download_template('elementor')
#     # cl.copy_to_workspace('elementor')
#     # cl.move_to_workspace('elementor')
#     # cl.delete_template('elementor')
#     # cl.search_template()
#     # cl.change_layout('layout')
#
#
# def test_profile(browser, read_credentials):
#     p = Profile(browser, read_credentials)
#     # now = datetime.now()
#     # name = now.strftime("%A")
#     # p.change_personal_info("Mr.", name)
#     # p.update_email('testerbhaai+1@gmail.com')
#     p.set_usr('user_1')
#     # p.change_password('user_1', '123ABC456def')
#     p.set_env('dev')
#     p.payment_method('5555 5555 5555 4444')
#     # p.payment_method_remove_delete_card()
#     # p.my_favorites('starter', 'block')
#     # p.my_downloads()
#
#
# def test_manage_api(browser):
#     api = ManageAPI(browser)
#     # api.create_token()
#     # api.copy_token()
#     # api.delete_token()
#     # api.create_token()
#
#
# def test_subscription(browser):
#     subs = Subscription(browser)
#     subs.set_env('dev')
#     # subs.check_subscription('monthly')
#     # subs.check_subscription('annual')
#     # subs.upgrade_package('premium', 'monthly')
#     # subs.upgrade_package('premium', 'yearly')
#     # subs.upgrade_package('lifetime')
#     # subs.pay_with_method('default')
#     # subs.chancel_renewal()
#     # subs.resume_subscription()
#     # subs.downgrade_package("starter")


def test_my_work(browser):
    browse_templates = BrowseTemplates(browser)
    browse_templates.testcase()

