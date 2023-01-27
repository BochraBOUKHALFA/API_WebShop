import requests
from flask import Flask, jsonify, request


def check_api_key():
    api_key = request.headers.get('API_KEY')
    if api_key != "BOCHRA":
        return "Invalid API Key", 401
    else:
        return None

