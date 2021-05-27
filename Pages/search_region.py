from Base.base_page import BasePage
from Pages.search_results_page import SearchResults
from Locators.search_locators import SearchLocators as SL

class SearchRegion(BasePage):

    def __init__(self,driver):
        super(SearchRegion,self).__init__(driver)

    def search_for(self,term):

        self.search_field = self.driver.find_element_by_name(SL.search_box_locator)
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()

        return SearchResults(self.driver)

