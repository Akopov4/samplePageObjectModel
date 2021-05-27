from base.base_page import BasePage, InvalidPageException
from locators.product_page_locators import ProductPageLocators as PPL


class ProductPage(BasePage):

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver)

    def name(self):
        return self.driver.find_element_by_css_selector(
            PPL.name_locator).text.strip()

    def description(self):
        return self.driver.find_element_by_css_selector(
            PPL.product_description_locator).text.strip()

    def stock_status(self):
        return self.driver.find_element_by_css_selector(
            PPL.product_stock_status_locator).text.strip()

    def price(self):
        return self.driver.find_element_by_css_selector(
            PPL.product_price_locator).text.strip()

    def _validate_page(self, driver):
        try:
            driver.find_element_by_css_selector(PPL.product_view_locator)
        except BaseException:
            raise InvalidPageException('Product page not loaded')
