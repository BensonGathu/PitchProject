from . import db
from datetime import datetime,timezone

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    image_path = db.Column(db.String(255))

    def __repr__(self):
       return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key=True)
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    up_vote = db.Column(db.Integer)
    down_vote = db.Column(db.Integer)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
      return f'User {self.pitch}'