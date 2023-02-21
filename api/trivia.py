# import json
# from flask import Blueprint, request, jsonify
# from flask_restful import Api, Resource # used for REST API building
# from datetime import datetime
# import random

# from model.QATrivia import User

# user_api = Blueprint('user_api', __name__,
#                    url_prefix='/api/users')

# # API docs https://flask-restful.readthedocs.io/en/latest/api.html
# api = Api(user_api)

# class UserAPI:
#     class _Create(Resource):
#         def post(self):
#             ''' Read data for json body '''
#             body = request.get_json()
            
#             # ''' Avoid garbage in, error checking '''
#             # # validate name
#             question = body.get('question')
#             # if question is None or len(question) < 2:
#             #     return {'message': f'Question is missing, or is less than 2 characters'}, 400
#             # # validate correct answer
#             correctAnswer = body.get('correctAnswer')
#             # if correctAnswer is None or len(correctAnswer) == 0:
#             #     return {'message': f'answer is missing'}, 400
#             # ''' #1: Key code block, setup USER OBJECT '''
#             # uo = User(question=question, 
#             #           correctAnswer=correctAnswer)
#             # # validate incorrect answers
#             incorrectAnswer1 = body.get('incorrectAnswer1')
#             # if incorrectAnswer1 is None or len(incorrectAnswer1) == 0:
#             #     return {'message': f'answer is missing'}, 400
#             # ''' #1: Key code block, setup USER OBJECT '''
#             # uo = User(question=question, 
#             #           incorrectAnswer1=incorrectAnswer1)     
            
#             incorrectAnswer2 = body.get('incorrectAnswer2')
#             # if incorrectAnswer2 is None or len(incorrectAnswer2) == 0:
#             #     return {'message': f'answer is missing'}, 400
#             # ''' #1: Key code block, setup USER OBJECT '''
#             # uo = User(question=question, 
#             #           incorrectAnswer1=incorrectAnswer1,
#             #           incorrectAnswer2=incorrectAnswer2)
                      
#             incorrectAnswer3 = body.get('incorrectAnswer3')
#             # if incorrectAnswer3 is None or len(incorrectAnswer3) == 0:
#             #     return {'message': f'answer is missing'}, 400
#             # ''' #1: Key code block, setup USER OBJECT '''
#             uo = User(question=question, 
#                       correctAnswer=correctAnswer,
#                       incorrectAnswer1=incorrectAnswer1,
#                       incorrectAnswer2=incorrectAnswer2,
#                       incorrectAnswer3=incorrectAnswer3)       
            
#             ''' #2: Key Code block to add user to database '''
#             # create user in database
#             user = uo.create()
#             # success returns json of user
#             if user:
#                 return jsonify(user.read())
#             # failure returns error
#             return {'message': f'Processed {question}, format error'}, 400        
#     class _Read(Resource):
#         def get(self):
#             users = User.query.all()    # read/extract all users from database
#             random.shuffle(users)
#             user = users[0]
#             # json_ready = [user.read() for user in users]  # prepare output in json
#             return jsonify(user.read())  # jsonify creates Flask response object, more specific to APIs than json.dumps

# # building RESTapi endpoint
#     api.add_resource(_Create, '/create')
#     api.add_resource(_Read, '/')



# # this should work
    
    
import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
import random

from model.QATrivia import QA

trivia_api = Blueprint('trivia_api', __name__,
                   url_prefix='/api/trivia')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(trivia_api)

class triviaAPI:
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            # ''' Avoid garbage in, error checking '''
            # # validate name
            question = body.get('question')
            # if question is None or len(question) < 2:
            #     return {'message': f'Question is missing, or is less than 2 characters'}, 400
            # # validate correct answer
            correctAnswer = body.get('correctAnswer')
            # if correctAnswer is None or len(correctAnswer) == 0:
            #     return {'message': f'answer is missing'}, 400
            # ''' #1: Key code block, setup USER OBJECT '''
            # uo = User(question=question, 
            #           correctAnswer=correctAnswer)
            # # validate incorrect answers
            incorrectAnswer1 = body.get('incorrectAnswer1')
            # if incorrectAnswer1 is None or len(incorrectAnswer1) == 0:
            #     return {'message': f'answer is missing'}, 400
            # ''' #1: Key code block, setup USER OBJECT '''
            # uo = User(question=question, 
            #           incorrectAnswer1=incorrectAnswer1)     
            
            incorrectAnswer2 = body.get('incorrectAnswer2')
            # if incorrectAnswer2 is None or len(incorrectAnswer2) == 0:
            #     return {'message': f'answer is missing'}, 400
            # ''' #1: Key code block, setup USER OBJECT '''
            # uo = User(question=question, 
            #           incorrectAnswer1=incorrectAnswer1,
            #           incorrectAnswer2=incorrectAnswer2)
                      
            incorrectAnswer3 = body.get('incorrectAnswer3')
            # if incorrectAnswer3 is None or len(incorrectAnswer3) == 0:
            #     return {'message': f'answer is missing'}, 400
            # ''' #1: Key code block, setup USER OBJECT '''
            uo = QA(question=question, 
                      correctAnswer=correctAnswer,
                      incorrectAnswer1=incorrectAnswer1,
                      incorrectAnswer2=incorrectAnswer2,
                      incorrectAnswer3=incorrectAnswer3)       
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            qA = uo.create()
            # success returns json of user
            if qA:
                return jsonify(qA.read())
            # failure returns error
            return {'message': f'Processed {question}, format error'}, 400        
    class _Read(Resource):
        def get(self):
            qAs = QA.query.all()    # read/extract all users from database
            random.shuffle(qAs)
            qA = qAs[0]
            # json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(qA.read())  # jsonify creates Flask response object, more specific to APIs than json.dumps

# building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')


# this should work
    