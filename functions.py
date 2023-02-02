
def filter_stock(products, product_id):
    for product in products:
        if product['id'] == product_id and product['stock'] > 0:
            return product['stock']



def filter_order(custemers, custemer_id):
    for custemer in custemers:
        if custemer['id'] == custemer_id:
            return custemer['username'], custemer['orders']


def filter_custemer(custemers, custemer_id):
    for custemer in custemers:
        if custemer['id'] == custemer_id:
            return custemer
