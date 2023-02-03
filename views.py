import requests
from flask import Flask, jsonify, request
from key import check_api_key
from functions import filter_product, filter_stock, filter_order, filter_custemer, filter_stocks, \
    filter_custemers_orders
from config import KEY, END_POINT_ERP, END_POINT_CRM
from app import app

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
            filtered_product = filter_product(product,  product_id)
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

@app.route('/custemers/ordors', methods=['GET'])
def get_custemers_ordors():
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        custemer_orders = response.json()
        filtered_orders = filter_custemers_orders(custemer_orders)
        return jsonify(filtered_orders), response.status_code


@app.route('/ordor/<custemer_id>', methods=['GET'])
def get_ordor(custemer_id):
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        custemer = response.json()
        filtered_order = filter_order(custemer, custemer_id)
        return jsonify(filtered_order), response.status_code


@app.route('/custemers', methods=['GET'])
def get_custemers():
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        custemers = response.json()
        return jsonify(custemers), response.status_code


@app.route('/custemer/<custemer_id>', methods=['GET'])
def get_custemer(custemer_id):
    if check_api_key() is not None:
        return check_api_key()
    response = requests.get(END_POINT_CRM)
    if response.status_code != 200:
        return erreur + response.text, response.status_code
    else:
        custemer = response.json()
        filtered_custemer = filter_custemer(custemer, custemer_id)
        return jsonify(filtered_custemer), response.status_code
