"""For testing of this framework was used magento demo site  Madison Island.
There are couple of them available in the internet. I used web site of 2014 year"""

import pytest

from selenium import webdriver


def environment_options(parser):
    parser.addoption('--browser', '-B', dest='BROWSER', choises=['chrome', 'chr', 'firefox', 'ff'],
                     help=f"possible values are: {['chrome', 'chr', 'firefox', 'ff']}", required=True)

    parser.addoption('--server', '-S', dest="SERVER")


@pytest.fixture(scope='session')
def environment_set_up(request):
    if request.config.getoption("BROWSER") in ['chrome', 'chr']:
        driver = webdriver.Chrome()
    elif request.config.getoption("BROWSER") in ['firefox', 'ff']:
        driver = webdriver.Firefox()

    if request.config.getoption("SERVER") is not None:
