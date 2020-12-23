from flask import Flask, jsonify
from auth.auth import auth_api
from secure.secure import secure_api
# from flask_restful import Resource, Api


app = Flask(__name__)
# api = Api(app)


''' This api is created using flask_restful package--

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/helloworld')

--End '''


app.register_blueprint(auth_api, url_prefix="/auth")
app.register_blueprint(secure_api, url_prefix="/secure")


# this is the root route
@app.route('/')
def index():
    return jsonify("Hello World, This is the root!"), 200

