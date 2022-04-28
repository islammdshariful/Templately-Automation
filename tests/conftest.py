import json
import os
import sys

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def read_credentials(scope='session'):
    with open(str(sys.path[1]) + '/utils/credentials.json') as credentials:
        credential = json.load(credentials)

    return credential


@pytest.fixture()
def open_file(scope='session'):
    credentials = open(str(sys.path[1]) + '/utils/credentials.json')
    # with open(str(sys.path[1]) + '/utils/credentials.json') as credentials
    return credentials


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
    b.implicitly_wait('3')

    yield b

    # b.quit()
