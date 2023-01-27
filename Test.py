import unittest
from functions import filter_stock , filter_custemer , filter_order


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

class TestFilterOrder(unittest.TestCase):
    def test_filter_order_returns_correct_value(self):
        customers = [
            {'id': 4, 'username': 'kenza', 'orders': ['item1', 'item2']},
            {'id': 2, 'username': 'bochra', 'orders': ['item3']},
            {'id': 3, 'username': 'anis', 'orders': []}
        ]
        customer_id = 4
        expected_result = ('kenza', ['item1', 'item2'])
        self.assertEqual(filter_order(customers, customer_id), expected_result)

    def test_filter_order_returns_none_when_customer_not_found(self):
        customers = [
            {'id': 1, 'username': 'bochra', 'orders': ['item1', 'item2']},
            {'id': 2, 'username': 'juba', 'orders': ['item3']},
            {'id': 3, 'username': 'kenza', 'orders': []}
        ]
        customer_id = 5
        self.assertIsNone(filter_order(customers, customer_id))


class TestFilterCustemer(unittest.TestCase):
    def test_filter_custemer_returns_correct_value(self):
        custemers = [
            {'id': 1, 'username': 'bochra', 'orders': [1, 2, 3]},
            {'id': 2, 'username': 'kenza', 'orders': [4, 5]},
            {'id': 3, 'username': 'anis', 'orders': [6, 7, 8, 9]}
        ]
        custemer_id = 1
        expected_result = {'id': 1, 'username': 'bochra', 'orders': [1, 2, 3]}
        self.assertEqual(filter_custemer(custemers, custemer_id), expected_result)


if __name__ == '__main__':
    unittest.main()
