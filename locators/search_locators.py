from enum import Enum


class SearchLocators():
    product_list_locator = 'ul.products-grid > li'
    product_name_locator = 'h2.product-name a'
    product_image_link = 'a.product-image'
    page_title_locator = 'div.page-title'
    products_count = 0
    products = {}