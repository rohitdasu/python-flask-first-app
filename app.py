from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

#running flask app -> FLASK_APP=app.py FLASK_ENV=development flask run