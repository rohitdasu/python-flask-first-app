from flask import Blueprint, jsonify

secure_api = Blueprint("secure_api", __name__)

@secure_api.route('/')
def auth():
    return jsonify("This is secured API (Token should be passed)"), 200