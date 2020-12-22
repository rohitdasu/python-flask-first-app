from flask import Blueprint
from flask import request, abort

auth_api = Blueprint("auth_api", __name__)

@auth_api.route('/')
def auth():
    return "This is Auth API"

@auth_api.route('/signin', methods=['GET', 'POST'])
def signin():

    if request.method == 'GET':
        abort(400, "Invalid Request, Please send POST request")
    else:
        username = request.form['username'];
        password = request.form['password'];

        data = {
            "username": username,
            "password": password
        }

        return data;