import os
from app import app, models
from flask import render_template, request, redirect
from flask_pymongo import PyMongo
from app.models import model
from bson.objectid import ObjectId

# from flask_table import Table, Col

app.config['MONGO_DBNAME'] = 'StudyBuddy' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://sdebenedictis:gGoykirvIqC3AEN0@cluster0-iidqj.mongodb.net/StudyBuddy?retryWrites=true&w=majority' 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    collection = mongo.db.Form
    students = collection.find({})
    return render_template('index.html')


# CONNECT TO DB, ADD DATA

# @app.route('/add')

# def add():
#     # connect to the database
#     user = mongo.db.users
#     # insert new data
#     user.insert({'name':'Silvia'})
#     # return a message to the user
#     return "Added User!"
#     # insert new data


@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == "GET":
        return render_template('index.html')
    else:
        name_name = request.form['name'] 
        college_name = request.form['college']
        email_name = request.form['email']
        major_name = request.form['major']
        course_name = request.form['course']
        classes_name = request.form['classes']
        print('name')

        callcourse = model.search(college_name,course_name)
        date = callcourse['date']
        time = callcourse['time'] 
        time2 = callcourse['time2']
        time3 = callcourse['time3']
        time4 = callcourse['time4']
        time5 = callcourse['time5']
        location = callcourse ['location']
        print(callcourse)
        collection = mongo.db.Form
        # print(name
        collection.insert({'name': name_name, 'college': college_name, 'email':email_name, 'major': major_name, 'course': course_name, 'classes': classes_name})
        userInfo = collection.find_one({"name" : name_name})
        return render_template("results.html", userInfo = userInfo, date= date, time = time, time2 = time2, time3 = time3, time4 = time4, time5 = time5, location = location)
        
        
        
# @app.route('/options', methods = ['GET', 'POST'])
# def options():
#     if request.method == "GET":
#         return render_template('/options.html')
   
   
   
@app.route('/createeevent', methods = ['GET', 'POST'])
def createeevent():
    if request.method == "GET":
        return render_template('/options.html')
    else:
        name_name = request.form['name']
        college_name = request.form['college']
        course_name = request.form['course']
        time_name = request.form['times']
        dates_name = request.form['dates']
        des_name = request.form['description']

        # callcourse = model.search(college_name,course_name)
        # date = callcourse['date']
        # time = callcourse['time']
        # location = callcourse ['location']
        collection = mongo.db.Form
        
        collection.insert({'college': college_name, 'course': course_name, 'time': time_name, 'dates': dates_name ,'Description of the structure of the study group': des_name })
        # return render_template("options.html", college_name = college_name , course_name = course_name, dates_name = dates_name, time_name = time_name, des_name = des_name)
        return render_template('accepted.html')
     
     
        
        
        
    
@app.route('/confirm/<userID>', methods = ['GET', 'POST'])
def confirm(userID):
    if request.method == "GET":
        return render_template('results.html')
    else:
        collection = mongo.db.Form
        userInfo = collection.find_one({'_id' : ObjectId(userID)})
        time = request.form['time']
        return render_template("confirm.html", userInfo= userInfo, time= time)
        
@app.route('/options', methods = ['GET', 'POST'])
def page():
    if request.method == "POST":
        return render_template('options.html')
    else:
        return render_template("confirm.html")


# def event(eventID):
#     collection = mongo.db.events
#     event = collection.find_one({'_id' : ObjectId(eventID)})
#     return render_template('event.html', event = event)