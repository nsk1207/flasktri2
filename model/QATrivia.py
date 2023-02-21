""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
class Post(db.Model):
    __tablename__ = 'posts'

    # Define the Notes schema
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text, unique=False, nullable=False)
    image = db.Column(db.String, unique=False)
    # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
    userID = db.Column(db.Integer, db.ForeignKey('qAs.id'))

    # Constructor of a Notes object, initializes of instance variables within object
    def __init__(self, id, note, image):
        self.userID = id
        self.note = note
        self.image = image

    # Returns a string representation of the Notes object, similar to java toString()
    # returns string
    def __repr__(self):
        return "Notes(" + str(self.id) + "," + self.note + "," + str(self.userID) + ")"

    # CRUD create, adds a new record to the Notes table
    # returns the object added or None in case of an error
    def create(self):
        try:
            # creates a Notes object from Notes(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Notes table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read, returns dictionary representation of Notes object
    # returns dictionary
    def read(self):
        # encode image
        path = app.config['UPLOAD_FOLDER']
        file = os.path.join(path, self.image)
        file_text = open(file, 'rb')
        file_read = file_text.read()
        file_encode = base64.encodebytes(file_read)
        
        return {
            "id": self.id,
            "userID": self.userID,
            "note": self.note,
            "image": self.image,
        }


# Define the User class to manage actions in the 'users' table
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) User represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL







class QA(db.Model):
    __tablename__ = 'qAs'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _question = db.Column(db.String(255), unique=False, nullable=False)
    _correctAnswer = db.Column(db.String(255), unique=False, nullable=False)
    _incorrectAnswer1 = db.Column(db.String(255), unique=False, nullable = False)
    _incorrectAnswer2 = db.Column(db.String(255), unique=False, nullable = False)
    _incorrectAnswer3 = db.Column(db.String(255), unique=False, nullable = False)

    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    posts = db.relationship("Post", cascade='all, delete', backref='users', lazy=True)

    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, question, correctAnswer, incorrectAnswer1, incorrectAnswer2, incorrectAnswer3):
        self._question = question    # variables with self prefix become part of the object, 
        self._correctAnswer = correctAnswer
        self._incorrectAnswer1 = incorrectAnswer1
        self._incorrectAnswer2 = incorrectAnswer2
        self._incorrectAnswer3 = incorrectAnswer3
        


    # a name getter method, extracts name from object
    @property
    def question(self):
        return self._question
    
    # a setter function, allows name to be updated after initial object creation
    @question.setter
    def question(self, name):
        self._question = name
    
    # a getter method, extracts email from object
    @property
    def correctAnswer(self):
        return self._correctAnswer
    
    # a setter function, allows name to be updated after initial object creation
    @correctAnswer.setter
    def correctAnswer(self, correctAnswer):
        self._correctAnswer = correctAnswer
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, correctAnswer):
        return self._correctAnswer == correctAnswer
    
        # a getter method, extracts email from object
    @property
    def incorrectAnswer1(self):
        return self._incorrectAnswer1
    
    # a setter function, allows name to be updated after initial object creation
    @incorrectAnswer1.setter
    def incorrectAnswer1(self, incorrectAnswer1):
        self._incorrectAnswer1 = incorrectAnswer1
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, incorrectAnswer1):
        return self._incorrectAnswer1 == incorrectAnswer1
    
    @property
    def incorrectAnswer2(self):
        return self._incorrectAnswer2
    
    # a setter function, allows name to be updated after initial object creation
    @incorrectAnswer2.setter
    def incorrectAnswer2(self, incorrectAnswer2):
        self._incorrectAnswer2 = incorrectAnswer2
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, incorrectAnswer2):
        return self._incorrectAnswer2 == incorrectAnswer2
    
    
    @property
    def incorrectAnswer3(self):
        return self._incorrectAnswer3
    
    # a setter function, allows name to be updated after initial object creation
    @incorrectAnswer3.setter
    def incorrectAnswer3(self, incorrectAnswer3):
        self._incorrectAnswer3 = incorrectAnswer3
        
    # check if uid parameter matches user id in object, return boolean
    def is_uid(self, incorrectAnswer3):
        return self._incorrectAnswer3 == incorrectAnswer3
    

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
            #"id": self.id,
            "question": self._question,
            "correctAnswer": self._correctAnswer,
            "incorrectAnswer1": self._incorrectAnswer1,
            "incorrectAnswer2": self._incorrectAnswer2,
            "incorrectAnswer3": self._incorrectAnswer3
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, question="", correctAnswer="", incorrectAnswer1 = "",  incorrectAnswer2 = "",  incorrectAnswer3 = ""):
        """only updates values with length"""
        if len(question) > 0:
            self.question = question
        if len(correctAnswer) > 0:
            self.correctAnswer = correctAnswer
        if len(incorrectAnswer1) > 0:
            self.incorrectAnswer1 = incorrectAnswer1
        if len(incorrectAnswer2) > 0:
            self.incorrectAnswer2 = incorrectAnswer2
        if len(incorrectAnswer3) > 0:
            self.incorrectAnswer3 = incorrectAnswer3
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
def initQAs():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        q1 = QA(question='what is a cpu?', correctAnswer='central processing unit', incorrectAnswer1 = 'coolant protection unit', incorrectAnswer2 = 'unit processor', incorrectAnswer3 = 'man idk')
        q2 = QA(question='what does html stand for?', correctAnswer='Hypertext Markup Language', incorrectAnswer1 = 'Hyperlink Maker Language', incorrectAnswer2 = 'Hyper Mail Markup', incorrectAnswer3 = 'Humphrey Man Table Lawnmower')
        q3 = QA(question='what do we use AWS for?', correctAnswer='Deployment', incorrectAnswer1 = 'Fortnite', incorrectAnswer2 = 'Minecraft', incorrectAnswer3 = 'Java')
        q4 = QA(question='how do we access linux on our machines?', correctAnswer='wsl', incorrectAnswer1 = 'pylance', incorrectAnswer2 = 'Mongodb', incorrectAnswer3 = 'ReactJS')
        q5 = QA(question='who is our teacher?', correctAnswer='mr. yeung', incorrectAnswer1 = 'jmort223', incorrectAnswer2 = 'nathanial kim', incorrectAnswer3 = 'sabine')
        q6 = QA(question='what does FUBAR stand for?', correctAnswer='[expletive] up beyond repair', incorrectAnswer1 = 'Flipped u before reprimanding', incorrectAnswer2 = 'Family Under Bad Analogies Reviewed', incorrectAnswer3 = 'huh?')
        q7 = QA(question='how many sprints have we gone through this year?', correctAnswer='23', incorrectAnswer1 = '1', incorrectAnswer2 = '18', incorrectAnswer3 = '52')
        q8 = QA(question='which is NOT an example of proper PII?', correctAnswer='Your car', incorrectAnswer1 = 'House address', incorrectAnswer2 = 'Bank codes', incorrectAnswer3 = 'Passwords')
        q9 = QA(question='what do we use for our databases?', correctAnswer='SQLAlchemy', incorrectAnswer1 = 'XML', incorrectAnswer2 = 'MongoDB', incorrectAnswer3 = 'NodeJS')
        q10 = QA(question='what would constitute as backend development?', correctAnswer='working with python to create things like a database.', incorrectAnswer1 = 'using HTML to create a webpage', incorrectAnswer2 = 'using CSS to style', incorrectAnswer3 = 'Deployment using a platform like AWS')
        qAs = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

        """Builds sample user/note(s) data"""
        for qA in qAs:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                    note = "#### " + qA.question + " note " + str(num) + ". \n Generated by test data."
                    qA.posts.append(Post(id=qA.id, note=note, image='ncs_logo.png'))
                '''add user/post data to table'''
                qA.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {qA.correctAnswer}")
            
