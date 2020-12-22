from flask import Flask
from auth.auth import auth_api
from secure.secure import secure_api

app = Flask(__name__)

app.register_blueprint(auth_api, url_prefix="/auth")
app.register_blueprint(secure_api, url_prefix="/secure")


# this is the root route
@app.route('/')
def index():
    return "Hello World, This is the root!", 200

