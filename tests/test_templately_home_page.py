from src.site.home.home_page import HomePage


def test_home_page(browser):
    home_page = HomePage(browser)
    home_page.load()
    home_page.testcase()
