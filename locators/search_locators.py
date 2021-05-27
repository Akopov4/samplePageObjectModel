from enum import Enum


class SearchLocators(Enum):
    search_box_locator = 'q'
    product_list_locator= 'ul.products-grid > li'
    product_name_locator = 'h2.product-name a'
    product_image_link = 'a.product-image'
    page_title_locator = 'div.page-title'
