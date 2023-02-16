import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
import random

from model.QATrivia import User

user_api = Blueprint('user_api', __name__,
                   url_prefix='/api/users')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(user_api)

class UserAPI:        
    class _Read(Resource):
        def get(self):
            users = User.query.all()    # read/extract all users from database
            random.shuffle(users)
            user = users[0]
            # json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(user.read())  # jsonify creates Flask response object, more specific to APIs than json.dumps

# building RESTapi endpoint
    api.add_resource(_Read, '/')


# this should work
    