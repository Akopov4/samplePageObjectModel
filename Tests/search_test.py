from Pages.home_page import HomePage
class SearchProductTest:

    def test_search_for_products(self):
        homepage = HomePage(self.driver)
        search_results = homepage.search.searchFor('earphones')
        self.assertEqual(3, search_results.product_count)
        product = search_results.open_product_page('MADISON EARBUDS')
        self.assertEqual('MADISON EARBUDS', product.name)
        self.assertEqual('$35.00', product.price)
        self.assertEqual('IN STOCK', product.stock_status)

