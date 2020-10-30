#!/usr/bin/python3

from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import cross_origin

from src.input_handler import handle_input, start_conversation
from src.users import add_user, find_user

import requests
import os

env = os.getenv('PYTHON_ENV', 'dev')

default_dir = './reports/' if env == 'dev' else '/tmp/reports/'

PORT = 8080 if 'PORT' not in os.environ else os.environ['PORT']
HOST = '127.0.0.1' if 'HOST' not in os.environ else os.environ['HOST']

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", ping_timeout=30)
app.config['DEBUG'] = True if PORT == 8080 else False


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/reports/<report_id>', methods=['GET'])
@cross_origin()
def download_report(report_id):
	filename = report_id + '.pdf'
	if not os.path.exists(default_dir + filename):
		return 'File does not exist', 400
	return send_from_directory(directory=default_dir, filename=filename)


@socketio.on('message')
def handle_message(message):
    user = find_user(request.sid)
    response = handle_input(user, message)
    emit('message', response)


@socketio.on('connect')
def handle_connect():
    add_user(request.sid)
    user = find_user(request.sid)
    response = start_conversation(user)
    emit('message', response)


@socketio.on('disconnect')
def disconnect():
    user = find_user(request.sid)
    print('User disconnected')


if __name__ == "__main__":
    socketio.run(app, host=HOST, port=PORT)
