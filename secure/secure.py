from flask import Blueprint

secure_api = Blueprint("secure_api", __name__)

@secure_api.route('/')
def auth():
    return "This is secured API (Token should be passed)", 200