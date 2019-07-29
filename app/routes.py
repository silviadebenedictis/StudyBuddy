import os
from app import app
from flask import render_template, request, redirect
from flask_pymongo import PyMongo

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

        collection = mongo.db.Form
        # print(name
        collection.insert({'name': name_name, 'college': college_name, 'email':email_name, 'major': major_name, 'course': course_name, 'classes': classes_name})
        return render_template("results.html", name_name = name_name , college_name = college_name ,email_name = email_name , major_name = major_name ,course_name = course_name, classes_name = classes_name)
        
