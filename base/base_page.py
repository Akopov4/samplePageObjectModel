


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.__validate_page(driver)

    def __validate_page(self, driver):
        return




class InvalidPageException(Exception):
    """Throw this exception when you don’t find the correct page"""
    pass
