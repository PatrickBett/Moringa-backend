from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

from datetime import datetime

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))

    def serialize(self):
        return {
            
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
            "role": self.role
        }
    

class Content(db.Model,SerializerMixin):
    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(350))
    content_type = db.Column(db.String(50))
    published_date = db.Column(db.DateTime, default=datetime.utcnow) 
    content_url = db.Column(db.String(250))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    flagged = db.Column(db.Boolean, default = False)
    status = db.Column(db.Boolean, default = True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))


class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    id =  db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(50), unique = True)

    
class Profile(db.Model,SerializerMixin):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key = True)
    profile_picture = db.Column(db.String)
    bio = db.Column(db.String(200))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


class Comment(db.Model,SerializerMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content_id = db.Column(db.Integer,db.ForeignKey('contents.id'))

class Wishlist(db.Model,SerializerMixin):
    __tablename__ = 'wishlists'
    id = db.Column(db.Integer, primary_key = True)
    content_id = db.Column(db.Integer,db.ForeignKey('contents.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Subscription(db.Model,SerializerMixin):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
class Recommendation(db.Model,SerializerMixin):
    __tablename__ = 'recommendations'
    id = db.Column(db.Integer, primary_key = True)
    content_id = db.Column(db.Integer, db.ForeignKey('contents.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    

