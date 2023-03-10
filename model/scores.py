""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db


from sqlalchemy.exc import IntegrityError



''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table


# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Scores(db.Model):
    __tablename__ = 'Scores'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(255), unique=False, nullable=False)
    _sid = db.Column(db.String(255), unique=True, nullable=False)
    _score = db.Column(db.String(255), unique=False, nullable=False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
   

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, name, sid, score):
        self._name = name    # variables with self prefix become part of the object, 
        self._sid = sid
        self._score = score
        
        

    # a name getter method, extracts name from object
    @property
    def name(self):
        return self._name
    
    # a setter function, allows name to be updated after initial object creation
    @name.setter
    def name(self, name):
        self._name = name
    
    # a getter method, extracts email from object
    @property
    def sid(self):
        return self._sid
    
    # a setter function, allows name to be updated after initial object creation
    @sid.setter
    def sid(self, sid):
        self._sid = sid
        
    # check if uid parameter matches user id in object, return boolean
    def is_sid(self, sid):
        return self._sid == sid
    

    
    
    # dob property is returned as string, to avoid unfriendly outcomes
    @property
    def score(self):
        return self._score
    
    # a setter function, allows name to be updated after initial object creation
    @score.setter
    def score(self, score):
        self._score = score



    
    
    # output content using str(object) in human readable form, uses getter
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "name": self.name,
            "sid": self.sid,
            
            "score": self.score
            
           
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, name="", sid="", score=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(sid) > 0:
            self.sid = sid
        if len(score) > 0:
            self.score = score
        
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing """


# Builds working data for testing
def initScores():
     with app.app_context():
         """Create database and tables"""
         
         db.create_all()
         """Tester data for table"""
         u1 = Scores(name='alyssa', sid='12345', score = 10)
         u2 = Scores(name="sabine", sid="ss", score = 20)
       

         scores = [u1, u2]

         """Builds sample user/note(s) data"""
         for score in scores:
             try:
                 score.create()
             except IntegrityError:
                 '''fails with bad or duplicate data'''
                 db.session.remove()
                 print(f"Duplicate email, or error: {score.sid}")

