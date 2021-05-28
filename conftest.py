"""For testing of this framework was used magento demo site  Madison Island.
There are couple of them available in the internet. I used web site of 2014 year"""

import pytest
import configparser
from selenium import webdriver
import os

def pytest_addoption(parser):
    parser.addoption('--browser', '-B', dest='BROWSER',
                     help=f"possible values are: {['chrome', 'chr', 'firefox', 'ff']}")

    parser.addoption('--server', '-S', dest="SERVER")


@pytest.fixture
def environment_configuration(request):
    read_config = configparser.ConfigParser()
    read_config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")
    # checking if browser was input from console or from config file from section Environment and assigment
    # it to browser_name variable
    browser_name = request.config.getoption(
        "BROWSER") or read_config.get('Environment','browser')

    # checking if remote server was input from console or from config file from section Environment and assigment
    # it to remote_server variable
    remote_server = request.config.getoption(
        "SERVER") or read_config.get('Environment','remote_server')

    driver = webdriver.Remote(
        command_executor=remote_server,
        desired_capabilities={
            "browserName": browser_name})
    driver.get("http://magento-demo.lexiconn.com/")

    yield driver
    driver.close()
