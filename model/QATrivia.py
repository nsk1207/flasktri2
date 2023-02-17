# """ database dependencies to support sqliteDB examples """
# from random import randrange
# from datetime import date
# import os, base64
# import json

# from __init__ import app, db
# from sqlalchemy.exc import IntegrityError
# from werkzeug.security import generate_password_hash, check_password_hash


# ''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# # Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
# class Post(db.Model):
#     __tablename__ = 'posts'

#     # Define the Notes schema
#     id = db.Column(db.Integer, primary_key=True)
#     note = db.Column(db.Text, unique=False, nullable=False)
#     image = db.Column(db.String, unique=False)
#     # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
#     userID = db.Column(db.Integer, db.ForeignKey('users.id'))

#     # Constructor of a Notes object, initializes of instance variables within object
#     def __init__(self, id, note, image):
#         self.userID = id
#         self.note = note
#         self.image = image

#     # Returns a string representation of the Notes object, similar to java toString()
#     # returns string
#     def __repr__(self):
#         return "Notes(" + str(self.id) + "," + self.note + "," + str(self.userID) + ")"

#     # CRUD create, adds a new record to the Notes table
#     # returns the object added or None in case of an error
#     def create(self):
#         try:
#             # creates a Notes object from Notes(db.Model) class, passes initializers
#             db.session.add(self)  # add prepares to persist person object to Notes table
#             db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
#             return self
#         except IntegrityError:
#             db.session.remove()
#             return None

#     # CRUD read, returns dictionary representation of Notes object
#     # returns dictionary
#     def read(self):
#         # encode image
#         path = app.config['UPLOAD_FOLDER']
#         file = os.path.join(path, self.image)
#         file_text = open(file, 'rb')
#         file_read = file_text.read()
#         file_encode = base64.encodebytes(file_read)
        
#         return {
#             "id": self.id,
#             "userID": self.userID,
#             "note": self.note,
#             "image": self.image,
#             "base64": str(file_encode)
#         }


# # Define the User class to manage actions in the 'users' table
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) User represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
# class User(db.Model):
#     __tablename__ = 'users'  # table name is plural, class name is singular

#     # Define the User schema with "vars" from object
#     id = db.Column(db.Integer, primary_key=True)
#     _name = db.Column(db.String(255), unique=False, nullable=False)
#     _uid = db.Column(db.String(255), unique=True, nullable=False)
#     _password = db.Column(db.String(255), unique=False, nullable=False)
#     _dob = db.Column(db.Date)

#     # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
#     posts = db.relationship("Post", cascade='all, delete', backref='users', lazy=True)

#     # constructor of a User object, initializes the instance variables within object (self)
#     def __init__(self, name, uid, password="123qwerty", dob=date.today()):
#         self._name = name    # variables with self prefix become part of the object, 
#         self._uid = uid
#         self.set_password(password)
#         self._dob = dob

#     # a name getter method, extracts name from object
#     @property
#     def name(self):
#         return self._name
    
#     # a setter function, allows name to be updated after initial object creation
#     @name.setter
#     def name(self, name):
#         self._name = name
    
#     # a getter method, extracts email from object
#     @property
#     def uid(self):
#         return self._uid
    
#     # a setter function, allows name to be updated after initial object creation
#     @uid.setter
#     def uid(self, uid):
#         self._uid = uid
        
#     # check if uid parameter matches user id in object, return boolean
#     def is_uid(self, uid):
#         return self._uid == uid
    
#     @property
#     def password(self):
#         return self._password[0:10] + "..." # because of security only show 1st characters

#     # update password, this is conventional setter
#     def set_password(self, password):
#         """Create a hashed password."""
#         self._password = generate_password_hash(password, method='sha256')

#     # check password parameter versus stored/encrypted password
#     def is_password(self, password):
#         """Check against hashed password."""
#         result = check_password_hash(self._password, password)
#         return result
    
#     # dob property is returned as string, to avoid unfriendly outcomes
#     @property
#     def dob(self):
#         dob_string = self._dob.strftime('%m-%d-%Y')
#         return dob_string
    
#     # dob should be have verification for type date
#     @dob.setter
#     def dob(self, dob):
#         self._dob = dob
    
#     @property
#     def age(self):
#         today = date.today()
#         return today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
    
#     # output content using str(object) in human readable form, uses getter
#     # output content using json dumps, this is ready for API response
#     def __str__(self):
#         return json.dumps(self.read())

#     # CRUD create/add a new record to the table
#     # returns self or None on error
#     def create(self):
#         try:
#             # creates a person object from User(db.Model) class, passes initializers
#             db.session.add(self)  # add prepares to persist person object to Users table
#             db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
#             return self
#         except IntegrityError:
#             db.session.remove()
#             return None

#     # CRUD read converts self to dictionary
#     # returns dictionary
#     def read(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "uid": self.uid,
#             "dob": self.dob,
#             "age": self.age,
#             "posts": [post.read() for post in self.posts]
#         }

#     # CRUD update: updates user name, password, phone
#     # returns self
#     def update(self, name="", uid="", password=""):
#         """only updates values with length"""
#         if len(name) > 0:
#             self.name = name
#         if len(uid) > 0:
#             self.uid = uid
#         if len(password) > 0:
#             self.set_password(password)
#         db.session.commit()
#         return self

#     # CRUD delete: remove self
#     # None
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
#         return None


# """Database Creation and Testing """


# # Builds working data for testing
# def initUsers():
#        with app.app_context():
#         """Create database and tables"""
#         db.init_app(app)
#         db.create_all()
#         """Tester data for table"""
#         u1 = User(name='Thomas Edison', uid='toby', password='123toby', dob=date(1847, 2, 11))
#         u2 = User(name='Nicholas Tesla', uid='niko', password='123niko')
#         u3 = User(name='Alexander Graham Bell', uid='lex', password='123lex')
#         u4 = User(name='Eli Whitney', uid='whit', password='123whit')
#         u5 = User(name='John Mortensen', uid='jm1021', dob=date(1959, 10, 21))

#         users = [u1, u2, u3, u4, u5]

#         """Builds sample user/note(s) data"""
#         for user in users:
#             try:
#                 '''add a few 1 to 4 notes per user'''
#                 for num in range(randrange(1, 4)):
#                     note = "#### " + user.name + " note " + str(num) + ". \n Generated by test data."
#                     user.posts.append(Post(id=user.id, note=note, image='ncs_logo.png'))
#                 '''add user/post data to table'''
#                 user.create()
#             except IntegrityError:
#                 '''fails with bad or duplicate data'''
#                 db.session.remove()
#                 print(f"Records exist, duplicate email, or error: {user.uid}")

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
    userID = db.Column(db.Integer, db.ForeignKey('users.id'))

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
class User(db.Model):
    __tablename__ = 'users'  # table name is plural, class name is singular

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
            "id": self.id,
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
def initUsers():
    with app.app_context():
        """Create database and tables"""
     
        db.create_all()
        """Tester data for table"""
        u1 = User(question='what is a cpu?', correctAnswer='central processing unit', incorrectAnswer1 = 'coolant protection unit', incorrectAnswer2 = 'unit processor', incorrectAnswer3 = 'man idk')
        u2 = User(question='what does html stand for?', correctAnswer='Hypertext Markup Language', incorrectAnswer1 = 'Hyperlink Maker Language', incorrectAnswer2 = 'Hyper Mail Markup', incorrectAnswer3 = 'Humphrey Man Table Lawnmower')
        u3 = User(question='what do we use AWS for?', correctAnswer='Deployment', incorrectAnswer1 = 'Fortnite', incorrectAnswer2 = 'Minecraft', incorrectAnswer3 = 'Java')
        u4 = User(question='how do we access linux on our machines', correctAnswer='wsl', incorrectAnswer1 = 'pylance', incorrectAnswer2 = 'Mongodb', incorrectAnswer3 = 'ReactJS')
        u5 = User(question='who is our teacher', correctAnswer='mr. yeung', incorrectAnswer1 = 'jmort223', incorrectAnswer2 = 'nathanial kim', incorrectAnswer3 = 'sabine')

        users = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for user in users:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 4)):
                    note = "#### " + user.question + " note " + str(num) + ". \n Generated by test data."
                    user.posts.append(Post(id=user.id, note=note, image='ncs_logo.png'))
                '''add user/post data to table'''
                user.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {user.correctAnswer}")
            
