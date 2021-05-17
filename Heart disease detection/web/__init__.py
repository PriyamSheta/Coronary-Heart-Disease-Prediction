from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='707ac90098c9527d9ba80beb68274cec'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/user'
db = SQLAlchemy(app)
login_manager=LoginManager(app)

from web import routes