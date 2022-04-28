from src.site.browse.browser import BrowseTemplates


def test_my_work(browser):
    browse_templates = BrowseTemplates(browser)
    browse_templates.search_with_popular_keys()
