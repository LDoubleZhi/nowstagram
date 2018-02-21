# -*- encoding=UTF-8 -*-

from nowstagram import app, db
from flask_script import Manager
from sqlalchemy import or_, and_
from nowstagram.models import User, Image, Comment
import random

manager = Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('User' + str(i),'a'+str(i)))
        for j in range(0, 7):
            db.session.add(Image(get_image_url(), i+1))
            for k in range(0, 3):
                db.session.add(Comment('This is a comment:' + str(k), 1+3*i+j, i+1))
    db.session.commit()
    #print 1, User.query.all()  #调用User的__repr__()方法

    # for i in range(50, 100, 2):
    #     user = User.query.get(i)
    #     user.username = '[New]' + user.username
    # db.session.commit()

    # print 2, user.images
    # image = Image.query.get(4)
    # print 3, image.user



if __name__ == '__main__':
    manager.run()
