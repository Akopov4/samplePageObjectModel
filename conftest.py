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
def environment_configuration(request):
    read_config = configparser.ConfigParser()
    # checking if browser was input from console or from config file from section Environment and assigment
    # it to browser_name variable

    browser_name = request.config.getoption(
        "BROWSER") or read_config.get("Environments", "browser")

    # checking if remote server was input from console or from config file from section Environment and assigment
    # it to remote_server variable
    remote_server = request.config.getoption(
        "SERVER") or read_config.get("Environments", "remote_server")

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
