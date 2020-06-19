#!/usr/bin/python3

from flask import Flask, request
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS, cross_origin

from src.input_handler import handle_input, start_conversation
from src.users import add_user, find_user

import requests
import os

application = Flask(__name__, static_url_path='/', static_folder='static/')
application.config['SECRET_KEY'] = 'secret!'
application.config['DEBUG'] = True
socketio = SocketIO()

PORT = 8080 if 'PORT' not in os.environ else os.environ['PORT']

socketio.init_app(application, cors_allowed_origins="*")

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
def test_disconnect():
    print('Client disconnected')

@application.route('/ui')
def send_html():
	return application.send_static_file('index.html')

@application.route('/')
def get_home():
	return 'Chat service online on port ' + str(PORT)

if __name__ == '__main__':
	print('Starting server')
	socketio.run(application, host='0.0.0.0', port=PORT)