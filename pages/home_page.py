from base.base_page import BasePage, InvalidPageException
from pages.search_region import SearchRegion
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)




    def __validate_page(self, driver):
        try:
            driver.find_element_by_class_name(HomePageLocators.home_page_slideshow_locator)


        except:
            raise InvalidPageException("Home Page not loaded")
    def search(self):
        return SearchRegion(self.driver)





