def filter_stock(products, product_id):
    for product in products:
        if product['id'] == product_id and product['stock'] > 0:
            return product['stock']


def filter_product(products, product_id):
    for product in products:
        if product['id'] == product_id and product['stock'] > 0:
            return product


def filter_stocks(products):
    product_names_and_stocks = []
    for product in products:
        product_names_and_stocks.append({
            "name": product["name"],
            "stock": product["stock"]
        })
    return product_names_and_stocks


def filter_order(customers, customer_id):
    for customer in customers:
        if customer['id'] == customer_id:
            return customer['username'], customer['orders']


def filter_product_order(customers, customer_id,orders, product_id):
    for customer in customers:
        if customer['id'] == customer_id:
            for order in orders:
                if order['id'] == product_id:
                    return order


def filter_customer(customers, customer_id):
    for customer in customers:
        if customer['id'] == customer_id:
            return customer


def filter_customers_orders(customers):
    customer_names_and_order = []
    for customer in customers:
        customer_names_and_order.append({
            "name": customer["name"],
            "orders": customer["orders"]
        })
    return customer_names_and_order


