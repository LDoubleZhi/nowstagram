# -*- encoding=UTF-8 -*-

from nowstagram import db, login_manager
import random
from datetime import  datetime
#from ImageSharing import login_manager

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1024))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer, default=0) # OK-0  Delete-1
    user = db.relationship('User')
    #backref属性可以双向

    def __init__(self, content, image_id, user_id):
        self.content = content
        self.image_id = image_id
        self.user_id = user_id

    def __repr__(self):
        return '<Comment %d %s>' % (self.id, self.content)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(512))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #一对多 多的一方通过外键关联
    created_date = db.Column(db.DateTime)
    comments = db.relationship('Comment')
    #对应多个comment
    def __init__(self, url, user_id):
        self.url = url
        self.user_id = user_id
        self.created_date = datetime.now()

    def __repr__(self):
        return '<Image %d %s>' % (self.id, self.url)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    #为了加密 加入salt
    salt = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    images = db.relationship('Image', backref = 'user', lazy = 'dynamic')
    #关系一对多 一个user对应多个image,可以在user对象中通过images属性获得用户所有图片

    def __init__(self, username, password, salt = ''):
        self.username = username #
        self.password = password
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
