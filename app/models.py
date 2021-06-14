from . import db
from datetime import datetime,timezone
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    image_path = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))
    pitches = db.relationship("Pitch",backref="user",lazy="dynamic")
    comment = db.relationship("Comment",backref="user",lazy="dynamic")
    up_vote =db.relationship("UpVotes",backref="user",lazy="dynamic")
    down_vote = db.relationship("DownVotes",backref="user",lazy="dynamic")

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
       return f'User {self.username}'


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    comment = db.relationship("Comment",backref="pitch",lazy="dynamic")
    up_vote = db.relationship("UpVotes",backref="pitch",lazy="dynamic")
    down_vote = db.relationship("DownVotes",backref="pitch",lazy="dynamic")
    category = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
      return f'Pitch: {self.pitch}'



# class Category(db.Model):
#     __tablename__ = 'category'
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(255))
#     pitch = db.relationship("Pitch",backref='category',lazy='dynamic')

#     def __repr__(self):
#       return f'Category: {self.name}'

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments
    def __repr__(self):
      return f'Comment: {self.comment}'




class UpVotes(db.Model):
    __tablename__='upvotes'
    id = db.Column(db.Integer,primary_key=True)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitch.id"))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_upvotes(cls,id):
        upvotes = UpVote.query.filter_by(pitch_id=id).all()
        return upvotes

    def __repr__(self):
      return f'Votes: {self.vote}'


class DownVotes(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
