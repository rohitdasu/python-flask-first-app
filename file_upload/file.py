import os
from flask import Flask
from werkzeug.utils import secure_filename
from flask import Blueprint, jsonify, request

current_directory = os.getcwd()

IMAGE_DIRECTORY = '/static/assets/images/'
UPLOAD_FOLDER = current_directory + IMAGE_DIRECTORY

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

file_api = Blueprint("file_api", __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_api.route('/', methods=['POST'])
def upload_file():

    if 'file' not in request.files:
        resp = jsonify({'success': False, 'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'success': False, 'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'success': True, 'message': 'File successfully uploaded!', 'img_url': request.host_url + IMAGE_DIRECTORY + filename})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'success': False, 'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp
