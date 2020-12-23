from flask import Blueprint, jsonify, request, abort

auth_api = Blueprint("auth_api", __name__)

@auth_api.route('/')
def auth():
    return jsonify("This is Auth API")


@auth_api.route('/signin', methods=['GET', 'POST'])
def signin():

    if request.method == 'GET':
        abort(400, "Invalid Request, Please send POST request")
        #or
        # return jsonify('Invalid Request, Please send POST request'), 400
    else:
        username = request.form['username'];
        password = request.form['password'];

        data = {
            "username": username,
            "password": password
        }

        return jsonify(data), 200 # it sends the status code 200