# -*- encoding=UTF-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
#这样可以在jinjia2里使用breakand continue了
app.config.from_pyfile('app.conf')
app.secret_key =  'nowcoder'
#app.config['SQLAlchemy_DATABASE_URI'] = 'mysql://root:@localhost:3306/test'
#通过配置文件进行配置，好处在于将配置信息集中处理
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = '/regloginpage/'
#设置没有权限时跳转到此页面

from nowstagram import views, models
