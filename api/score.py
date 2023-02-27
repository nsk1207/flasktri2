from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building


from model.scores import Scores

score_api = Blueprint('score_api', __name__,
                   url_prefix='/api/scores')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(score_api)

class ScoreAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate name
            name = body.get('name')
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 210
            # validate uid
            sid = body.get('sid')
            if sid is None or len(sid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            score = body.get('score')
            if score is None:
                return {'message': f'you have never played this game!'}, 210
            

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Scores(name=name, 
                      sid=sid,
                      score=score)
            
            ''' Additional garbage error checking '''
            # set password if provided
        
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            score = uo.create()
            # success returns json of user
            if score:
                return jsonify(score.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {sid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            scores = Scores.query.all()    # read/extract all users from database
            json_ready = [score.read() for score in scores]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')