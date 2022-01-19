import json
import os
import sys

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def config(scope='session'):
    with open(str(sys.path[1]) + '/utils/credentials.json') as cred:
        config = json.load(cred)

    return config


# This will run before all test case
@pytest.fixture(scope='module')
def browser():
    opts = Options()
    # opts.add_experimental_option("detach", True)
    opts.add_experimental_option('debuggerAddress', 'localhost:9250')
    b = webdriver.Chrome(str(os.getenv('chromedriver')), chrome_options=opts)
    # b = webdriver.Chrome(str(os.getenv('firefoxdriver')), chrome_options=opts)
    # b = webdriver.Chrome(chrome_options=opts)
    b.maximize_window()
    b.implicitly_wait('10')

    yield b

    # b.quit()
