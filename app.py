from main import app
import os

if __name__ == '__main__':

    port = int(os.environ.get("PORT", 33507))

    app.run(host='0.0.0.0', debug=True, port=port)

# running flask app -> FLASK_APP=app.py FLASK_ENV=development flask run
