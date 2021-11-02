import json
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

CORS(app)

db = SQLAlchemy(app)



class User(db.Model):
    fullName = db.Column( db.String, primary_key = True)
    grade = db.Column(db.Integer, nullable = False)

    def __init__(self, name, grade):
        self.fullName = name
        self.grade = grade

@app.route('/grades')
def get_grades():
    returnDict = {}
    arr = User.query.all()
    for users in arr:
        returnDict.update({users.fullName: users.grade})
    return returnDict

@app.route('/grades/<sname>')
def find_grade(sname):
    u = User.query.filter_by(fullName=sname).first()
    return {u.fullName: u.grade}

@app.route('/grades', methods=["POST"])
def input_grades():
    data = request.get_json()
    db.session.add(User(data["name"], data["grade"]))
    db.session.commit()
    returnDict = {}
    arr = User.query.all()
    for users in arr:
        returnDict.update({users.fullName: users.grade})
    return returnDict

@app.route('/grades/<sname>', methods=["PUT"])
def update_grade(sname):
    data = request.get_json()
    u = User.query.filter_by(fullName=sname).first()
    u.grade = data["grade"]
    db.session.commit()
    returnDict = {}
    arr = User.query.all()
    for users in arr:
        returnDict.update({users.fullName: users.grade})
    return returnDict

@app.route('/grades/<sname>', methods=["DELETE"])
def del_grade(sname):
    u = User.query.filter_by(fullName=sname).first()
    db.session.delete(u)
    db.session.commit()
    returnDict = {}
    arr = User.query.all()
    for users in arr:
        returnDict.update({users.fullName: users.grade})
    return returnDict


db.create_all()
app.run()