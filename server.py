#!/usr/bin/python3

from flask import Flask, render_template
from flask_socketio import SocketIO
import json


from src.input_handler import handle_input, start_conversation
from src.users import add_user, find_user

import requests
import os

PORT = 8080 if 'PORT' not in os.environ else os.environ['PORT']

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
	return app.send_static_file('index.html')

@socketio.on('message')
def handle_source(json_data):
  socketio.emit('message', 'mdrrr')

if __name__ == "__main__":
  socketio.run(app)