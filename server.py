#!/usr/bin/python3

from flask import Flask, request
from flask_socketio import SocketIO, emit

from src.input_handler import handle_input, start_conversation
from src.users import add_user, find_user

import requests
import os

PORT = 8080 if 'PORT' not in os.environ else os.environ['PORT']

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['DEBUG'] = True if PORT == 8080 else False


@app.route("/")
def index():
    return app.send_static_file('index.html')


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
    socketio.run(app, port=PORT)
