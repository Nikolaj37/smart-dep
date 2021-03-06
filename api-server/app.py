import json
import random
import time
from threading import Thread, Event

from flask import Flask, request
from flask_restplus import Resource, Namespace, Api, fields
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from sockets import socketio
from api_v1 import api as ns

app = Flask(__name__)
app.config.from_object('config')

socketio.init_app(app)

api = Api(app)
api.add_namespace(ns)

CORS(app, resources={r"/api/*": {"origins": "*"}})

if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=True)
