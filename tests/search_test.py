from pages.home_page import HomePage
import pytest



def test_search_for_products(environment_configuration):
        homepage = HomePage(environment_configuration)
        search_results = homepage.search().search_for('earphones')
        assert 1 == search_results.product_count
        product = search_results.open_product_page('MADISON EARBUDS')
        assert product.name == 'MADISON EARBUDS'
        assert product.price == '$35.00'
        assert product.stock_status == 'IN STOCK'

