from flask import Blueprint

auth_api = Blueprint("auth_api", __name__)

@auth_api.route('/')
def auth():
    return "This is Auth API"