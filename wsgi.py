from main import app

if __name__ == '__main__':
    app.run(debug=False)

#running flask app -> FLASK_APP=wsgi.py FLASK_ENV=development flask run