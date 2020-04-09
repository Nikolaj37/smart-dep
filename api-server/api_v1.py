import json
import random
import time
from threading import Thread, Event

from flask import request, current_app
from flask_restplus import Resource, Namespace, fields
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

api = Namespace('api/v1', description="Main API namespace")

_model_state = api.model('State', {
    'device_id': fields.String,
    'type': fields.String
})

_model_light = api.inherit('Light', _model_state, {
    'state': fields.Nested(api.model('LightState', {
        'enabled': fields.Boolean
    })
    ),
})

_model_power = api.inherit('Power', _model_state, {
    'state': fields.Nested(api.model('PowerState', {
        'enabled': fields.Boolean
    })
    ),
})

_powers_db = [
    {
        'device_id': '0',
        'type': 'power',
        'state': {
            'enabled': True
        }
    },
    {
        'device_id': '1',
        'type': 'power',
        'state': {
            'enabled': False
        }
    },
]


@api.route('/room/<string:place_id>/powers', endpoint='powers')
@api.param('place_id', 'ID of place')
class PowerUnits(Resource):
    @api.marshal_with(_model_power, as_list=True)
    def get(self, place_id):
        if current_app.debug:
            return _powers_db
        else:
            # TODO - db request required
            return {}


_lights_db = [
    {
        'device_id': '0',
        'type': 'light',
        'state': {
            'enabled': True
        }
    }
]


@api.route('/room/<string:place_id>/lights', endpoint='lights')
@api.param('place_id', 'ID of place')
class LightUnits(Resource):
    @api.marshal_with(_model_light, as_list=True)
    def get(self, place_id):
        if current_app.debug:
            return _lights_db
        else:
            # TODO - db request required
            return {}


_rooms_db = [
    {
        'id': '8201',
        'name': "KEMZ",
    }
]


_model_rooms = api.model('Room', {
    'id': fields.String,
    'name': fields.String,
})


@api.route('/rooms', endpoint='rooms')
class Rooms(Resource):
    @api.marshal_with(_model_rooms, as_list=True)
    def get(self):
        if current_app.debug:
            return _rooms_db
        else:
            # TODO - db request required
            return {}