from base.base_page import BasePage
from pages.search_results_page import SearchResults
from locators.search_locators import SearchLocators as SL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchRegion(BasePage):

    def __init__(self,driver):
        super(SearchRegion,self).__init__(driver)

    def search_for(self,term):

        # self.search_field = self.driver.find_element_by_name(SL.search_box_locator)
        self.search_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME,'q')))
        self.search_field.clear()
        self.search_field.send_keys(term)
        self.search_field.submit()

        return SearchResults(self.driver)

