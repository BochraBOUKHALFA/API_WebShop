def filter_stock(products, product_id):
    for product in products:
        if product['id'] == product_id and product['stock'] > 0:
            return product['stock']


def filter_product(products, product_id):
    for product in products:
        if product['id'] == product_id and product['stock'] > 0:
            return product.json


def filter_stocks(products):
    product_names_and_stocks = []
    for product in products:
        product_names_and_stocks.append({
            "name": product["name"],
            "stock": product["stock"]
        })
    return product_names_and_stocks


def filter_order(custemers, custemer_id):
    for custemer in custemers:
        if custemer['id'] == custemer_id:
            return custemer['username'], custemer['orders']


def filter_custemer(custemers, custemer_id):
    for custemer in custemers:
        if custemer['id'] == custemer_id:
            return custemer


def filter_custemers_ordors(custemers):
    custemer_names_and_ordor = []
    for custemer in custemers:
        custemer_names_and_ordor.append({
            "name": custemer["name"],
            "stock": custemer["stock"]
        })
    return custemer_names_and_ordor
