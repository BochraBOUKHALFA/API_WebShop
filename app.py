import requests
from flask import Flask, jsonify, request
from key import check_api_key
from functions import filter_product, filter_stock, filter_order, filter_customer, filter_stocks, \
    filter_customers_orders
from config import  END_POINT_ERP, END_POINT_CRM

app = Flask(__name__)

app.before_request(check_api_key)

erreur = "Error: "


@app.route('/products', methods=['GET'])
def get_products_info():
    request.headers.get('API_KEY')
    if check_api_key() is not None:
        return check_api_key()
    else:
        response = requests.get(END_POINT_ERP)
        if response.status_code != 200:
            return erreur + response.text, response.status_code
        else:
            product_info = response.json()
            return jsonify(product_info), response.status_code


@app.route('/product/<product_id>', methods=['GET'])
def get_product_info(product_id):
    request.headers.get('API_KEY')
    if check_api_key() is not None:
        return check_api_key()
    else:
        endpoint_url = END_POINT_ERP
        response = requests.get(endpoint_url)
        if response.status_code != 200:
            return erreur + response.text, response.status_code
        else:
            product = response.json()
            filtered_product = filter_product(product, product_id)
            return jsonify(filtered_product), response.status_code


@app.route('/products/stock', methods=['GET'])
def get_products_stock():
    if check_api_key() is not None:
        return check_api_key()
    else:
        response = requests.get(END_POINT_ERP)
        if response.status_code != 200:
            return erreur + response.text, response.status_code
        else:
            product = response.json()
            filtered_stock_name = filter_stocks(product)
            return jsonify(filtered_stock_name), response.status_code


@app.route('/product/stock/<product_id>', methods=['GET'])
# should add the key here
def get_product_stock(product_id):
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_ERP)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        product = response.json()
        filtered_stock = filter_stock(product, product_id)
        return jsonify(filtered_stock), response.status_code


# CRM

@app.route('/customers/orders', methods=['GET'])
def get_customers_orders():
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        customer_orders = response.json()
        filtered_orders = filter_customers_orders(customer_orders)
        return jsonify(filtered_orders), response.status_code


@app.route('/<customer_id>/ordor', methods=['GET'])
def get_order(customer_id):
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        order = response.json()
        filtered_order = filter_order(order, customer_id)
        return jsonify(filtered_order), response.status_code


@app.route('/<customer_id>/orders/<order_id>/products', methods=['GET'])
def get_product_order(customer_id, order_id):
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(
        f"https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers/{customer_id}/orders/{order_id}/products")
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        orders = response.json()
        return jsonify(orders), response.status_code


@app.route('/customers', methods=['GET'])
def get_customers():
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        customers = response.json()
        return jsonify(customers), response.status_code


@app.route('/customer/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        customer = response.json()
        filtered_customer = filter_customer(customer, customer_id)
        return jsonify(filtered_customer), response.status_code


if __name__ == '__main__':
    app.run()
