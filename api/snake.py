from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building


from model.snakes import Snakes

snake_api = Blueprint('snake_api', __name__,
                   url_prefix='/api/snake')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(snake_api)

class UserAPI:        
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
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            snakescore = body.get('snakescore')
            if snakescore is None:
                return {'message': f'you have never played this game!'}, 210
            

            ''' #1: Key code block, setup USER OBJECT '''
            so = Snakes(name=name, 
                      uid=uid,
                      snakescore=snakescore)
            
            ''' Additional garbage error checking '''
            # set password if provided
        
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            snake = so.create()
            # success returns json of user
            if snake:
                return jsonify(snake.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {uid} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            snakes = Snakes.query.all()    # read/extract all users from database
            json_ready = [snake.read() for snake in snakes]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
        
    class _Update(Resource):
        def put(self):
            ''' Read data for json body '''
            body = request.get_json()

            ''' Avoid garbage in, error checking '''
            # validate uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for password and dob
            new_snakescore = body.get('snakescore')
            if new_snakescore is None:
                return {'message': f'Snake score is missing'}, 210

            ''' #1: Key code block, lookup USER OBJECT '''
            snake = Snakes.query.filter_by(uid=uid).first()
            if snake is None:
                return {'message': f'User with User ID {uid} not found'}, 210

            ''' Additional garbage error checking '''
            # set password if provided

            ''' #2: Key Code block to update user in database '''
            # update user in database
            snake.update(snakescore=new_snakescore)
            # success returns json of updated user
            return jsonify(snake.read())

    class _Delete(Resource):
        def delete(self):
            ''' Read data for json body '''
            body = request.get_json()

            ''' Avoid garbage in, error checking '''
            # validate uid
            uid = body.get('uid')
            if uid is None or len(uid) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210

            ''' #1: Key code block, lookup USER OBJECT '''
            snake = Snakes.query.filter_by(uid=uid).first()
            if snake is None:
                return {'message': f'sorry! record doesnt exist'}

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Update, '/update')
    api.add_resource(_Delete, '/delete')