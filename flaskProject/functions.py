import requests
from flask import Flask, jsonify, request
from Key import check_api_key


def filter_stock(products, product_id):
    for product in products:
        if product['id'] == product_id and product['stock'] > 0:
            return product['stock']


def filter_ordor(custemers, custemer_id):
    for custemer in custemers:
        if custemer['id'] == custemer_id:
            return custemer['username'], custemer['orders']
        """else:
            return "product doesnt exist or it's out of stock"""
