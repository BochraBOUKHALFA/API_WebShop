import requests
from flask import Flask, jsonify, request
from Key import check_api_key
from functions import filter_stock, filter_ordor


app = Flask(__name__)

app.before_request(check_api_key)


@app.route('/products', methods=['GET'])
def get_product_info():
    api_key = request.headers.get('API_KEY')
    if check_api_key() is not None:
        return check_api_key()
    else:
        endpoint_url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/products/"
        response = requests.get(endpoint_url)
        if response.status_code != 200:
            return "Error: " + response.text, response.status_code
        else:
            product_info = response.json()
            return jsonify(product_info), response.status_code


@app.route('/product/stock/<product_id>', methods=['GET'])
# should add the key here
def get_product_stock(product_id):
    endpoint_url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/products/"
    response = requests.get(endpoint_url)
    if response.status_code != 200:
        return "Error: " + response.text, response.status_code
    else:
        product = response.json()
        filtered_stock = filter_stock(product, product_id)
        return jsonify(filtered_stock), response.status_code


@app.route('/ordor/<custemer_id>', methods=['GET'])
# and here to
def get_ordor(custemer_id):
    endpoint_url = "https://615f5fb4f7254d0017068109.mockapi.io/api/v1/customers"
    response = requests.get(endpoint_url)
    if response.status_code != 200:
        return "Error: " + response.text, response.status_code
    else:
        custemer = response.json()
        filtered_ordor = filter_ordor(custemer, custemer_id)
        return jsonify(filtered_ordor), response.status_code


if __name__ == '__main__':
    app.run()
