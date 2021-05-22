"""For testing of this framework was used magento demo site  Madison Island.
There are couple of them available in the internet. I used web site of 2014 year"""

import pytest
import configparser
from selenium import webdriver


def environment_options(parser):
    parser.addoption('--browser', '-B', dest='BROWSER', choises=['chrome', 'chr', 'firefox', 'ff'],
                     help=f"possible values are: {['chrome', 'chr', 'firefox', 'ff']}")

    parser.addoption('--server', '-S', dest="SERVER")


@pytest.fixture(scope='class')
def browser(request):
    read_config = configparser.ConfigParser()
    desired_capabilities = dict()

    browser_name = None
    remote_server = None

    # if remote server was  from terminal
    if request.config.getoption("SERVER"):
        remote_server = request.config.getoption("SERVER")

    # if  remote server was from config
    elif read_config.get("Environments", "remote_server"):
        remote_server = read_config.get("Environments", "remote_server")
    else:
        print("Please input server")

    # if browser was from terminal
    if request.config.getoption("BROWSER"):
        if request.config.getoption("BROWSER") in ['chrome', 'chr']:
            browser_name = "chrome"

        elif request.config.getoption("BROWSER") in ['firefox', 'ff']:
            browser_name = "firefox"
    # if browser was from config
    elif read_config.get("Environments", "remote_server"):
        browser_name = read_config.get("Environments", "remote_server")

    try:
        request.cls.driver = webdriver.Remote(
            command_executor=remote_server,
            desired_capabilities={
                "browserName": browser_name})
    except BaseException:
        print("check browser or remote server configs")

    yield request.cls.driver

    request.cls.driver.close()
    request.cls.driver.quit()
