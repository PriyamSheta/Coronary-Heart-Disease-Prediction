from datetime import datetime
from web import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(email):
    return People.query.get(email)

class People(db.Model,UserMixin):
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(20), nullable=False)

class Details(db.Model,UserMixin):
    user_id= db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    age = db.Column(db.String(20), nullable=False)
    current_smoker = db.Column(db.String(20), nullable=False)
    cigsperday = db.Column(db.String(20), nullable=False)
    bpmeds = db.Column(db.String(20), nullable=False)
    prevalentstroke = db.Column(db.String(20), nullable=False)
    prevalenthyp = db.Column(db.String(20), nullable=False)
    diabetes = db.Column(db.String(20), nullable=False)
    cholesterol = db.Column(db.String(20), nullable=False)
    sysbp = db.Column(db.String(20), nullable=False)
    diabp = db.Column(db.String(20), nullable=False)
    bmi = db.Column(db.String(20), nullable=False)
    heartrate = db.Column(db.String(20), nullable=False)
    glucose = db.Column(db.String(20), nullable=False)
    probability = db.Column(db.Float(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False, primary_key=True)
    
    
class Doctors(db.Model,UserMixin):
    name = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    contact = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(40), primary_key=True)
      