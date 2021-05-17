from flask import render_template, url_for, flash, redirect, request
from web import app
from web.forms import RegistrationForm, LoginForm
import numpy as np
import datetime
from flask_login import login_user
import requests
import pickle
from web import app, db
from web.models import People,Details,Doctors
file=open('My_Model_Logistic.pkl','rb')
parameters=pickle.load(file)

def sigmoid(z):
    y_head = 1/(1+ np.exp(-z))
    return y_head 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/home_2')
def home_2():
    return render_template('home_2.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        global e
        e=form.email.data
        user = People(username=form.username.data, email=form.email.data, password=form.password.data)
        
        authentic = People.query.filter_by(email=form.email.data).first()
        if authentic:
            flash(f'Account already created for {form.email.data}!', 'danger')
            return render_template('register.html', form=form)
        else:
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home_2'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        global e
        e=form.email.data
        user = People.query.filter_by(email=form.email.data,password=form.password.data).first()
        if user:
            return redirect(url_for('home_2'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/history')
def history():
    user = Details.query.filter_by(user_id=e).all()
    return render_template('history.html',details=user)

@app.route('/city')
def city():
    return render_template('city.html',probability=probability)

@app.route('/doctors',methods=['GET', 'POST'])
def doctors():
    city_user=request.form['city']
    doctors_city = Doctors.query.filter_by(city=city_user).all()
    return render_template('doctors.html',doctors=doctors_city)
          

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/Calculate.htm/bmi")
def bmi():
    return render_template('bmi.html')

@app.route('/Calculate.htm')
def calc():
    return render_template('calculate.htm')

@app.route('/Calculate.htm/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender=request.form['Gender']
        Age=request.form['age']
        Current_smoker=request.form['currentsm']
        Cigarete=request.form['cigsperday']
        BP_medication=request.form['BpMeds']
        Prevalent_Stroke=request.form['PrevalentStroke']
        Prevalent_Hypertensive=request.form['PrevalentHyp']
        Diabetes=request.form['Diabetes']
        Cholesterol=request.form['TopCol']
        SBP=request.form['Sbp']
        DBP=request.form['Dbp']
        BMI=request.form['BMI']
        Heart_rate=request.form['HRate']
        Glucose=request.form['Gluc']
        X=np.array([(Gender,Age,Current_smoker,Cigarete,BP_medication,Prevalent_Stroke,Prevalent_Hypertensive,Diabetes,Cholesterol,SBP,DBP,BMI,Heart_rate,Glucose)],dtype=np.float32)
        X=X.reshape(X.shape[0],-1).T        
        
        
        X[8]=(X[8]-107)/(696-107)
        X[9]=(X[9]-83.5)/(295-83.5)

        X[10]=(X[10]-48)/(142.5-48)

        X[11]=(X[11]-15.54)/(56.8-15.54)

        X[12]=(X[12]-44)/(143-44)
        X[13]=(X[13]-40)/(394-40)
        X[1]/=10
        X[3]/=10
        global probability
        probability = sigmoid((np.dot(parameters['weight'].T,X)+parameters['bias']))
        
        values= Details(user_id=e, gender=Gender, age=Age, current_smoker=Current_smoker, cigsperday=Cigarete, bpmeds=BP_medication, prevalentstroke=Prevalent_Stroke, prevalenthyp=Prevalent_Hypertensive, diabetes=Diabetes, cholesterol=Cholesterol, sysbp=SBP, diabp=DBP, bmi=BMI, heartrate=Heart_rate, glucose=Glucose, probability=round(probability[0][0],3), date=datetime.datetime.now())
        
        db.session.add(values)
        db.session.commit()
        
        probability=round(probability[0][0],3)
        if probability>0.57:
            text="Considered as HIGH risk."
            return redirect(url_for('city'))
        else:
            text="Considered as LOW risk."
            
        return render_template('Calculate.htm',prediction_text=" {}".format(probability),risk_text=text)
