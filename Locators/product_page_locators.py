from enum import Enum

class ProductPageLocators(Enum):
    product_view_locator = 'div.product-view'
    product_name_locator = 'div.product-name span'
    product_description_locator = 'div.tab-content div.std'
    product_stock_status_locator = 'p.availability span.value'
    product_price_locator = 'span.price'
