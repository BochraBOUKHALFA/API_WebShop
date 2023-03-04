
from flask import request
from config import KEY


def check_api_key():
    api_key = request.args.get('API_KEY')
    if api_key != KEY:
        return "Invalid API Key", 401
    else:
        return None



