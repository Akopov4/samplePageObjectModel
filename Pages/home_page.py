from Base.base_page import BasePage
from Base.base_page import InvalidPageException
from Pages.search_region import SearchRegion
from Locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def __validate_page(self, driver):
        try:
            driver.find_element_by_class_name(HomePageLocators.home_page_slideshow_locator)

        except:
            raise InvalidPageException("Home Page not loaded")


