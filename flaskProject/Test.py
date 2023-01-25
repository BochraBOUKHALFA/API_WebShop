import unittest


def filter_stock(products, product_id):
    for product in products:
        if product['id'] == product_id and product['stock'] > 0:
            return product['stock']


class TestFilterStock(unittest.TestCase):
    def test_filter_stock_returns_correct_value(self):
        products = [
            {'id': 1, 'stock': 10},
            {'id': 2, 'stock': 0},
            {'id': 3, 'stock': 5}
        ]
        product_id = 1
        expected_result = 10
        self.assertEqual(filter_stock(products, product_id), expected_result)

    def test_filter_stock_returns_none_when_product_not_found(self):
        products = [
            {'id': 1, 'stock': 10},
            {'id': 2, 'stock': 0},
            {'id': 3, 'stock': 5}
        ]
        product_id = 5
        self.assertIsNone(filter_stock(products, product_id))


if __name__ == '__main__':
    unittest.main()
