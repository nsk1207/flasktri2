import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app, db # Definitions initialization

from model.snakes import initSnakes
from model.wordles import initWordles
from model.QATrivia import initQAs

# setup APIs
 # Blueprint import api definition
from api.wordle import wordle_api
from api.snake import snake_api
from api.trivia import trivia_api
#from api.user import user_api # Blueprint import api definition

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

# register URIs
 # register api routes
app.register_blueprint(wordle_api)
app.register_blueprint(snake_api)
app.register_blueprint(trivia_api)

#app.register_blueprint(user_api) # register api routes
app.register_blueprint(app_projects) # register app pages

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.before_first_request
def activate_job():
    initSnakes()
    initWordles()
    initQAs()
  



# this runs the application on the development server
if __name__ == "__main__":
    from flask_cors import CORS
    cors = CORS(app)
    # change name for testing

    app.run(debug=True, host="0.0.0.0", port="4444")
