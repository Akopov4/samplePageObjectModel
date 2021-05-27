from locators.search_locators import SearchLocators as SL
from base.base_page import BasePage, InvalidPageException
from pages.product_page import ProductPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResults(BasePage):
    _products_count = 0
    _products = {}

    def __init__(self, driver):
        super(SearchResults, self).__init__(driver)
        results = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,SL.product_list_locator)))

        for product in results:
            name = product.find_element_by_css_selector(
                SL.product_name_locator).text
            self._products[name] = product.find_element_by_css_selector(
                SL.product_image_link)

    def __validate_page(self, driver):
        if 'Search results for' not in driver.title:
            raise InvalidPageException('Search results not loaded')

    def product_count(self):
        return len(self._products)

    def get_products(self):
        return self._products

    def open_product_page(self, product_name):
        self._products[product_name].click()
        return ProductPage(self.driver)
