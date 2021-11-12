import json
from typing import Dict
from flask import Flask, render_template, request
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user, login_user, UserMixin, login_required



app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'my Pa$$word!!!'

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

admin = Admin(app, name='microblog', template_mode='bootstrap3')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, unique=False, nullable = False)
    password = db.Column(db.String, unique=False, nullable=False)
    is_active = True

    def __init__(self, id):
        self.id = id

    def check_password(self, inputPassword):
        return inputPassword == self.password

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)

class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String, unique=True, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey(Teachers.id), nullable=False)
    numEnrolled = db.Column(db.Integer, unique=False, nullable=False)
    capacity = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.String, unique=False, nullable=False)



admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Classes, db.session))
admin.add_view(ModelView(Teachers, db.session))

db.create_all()
db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    try:
        u = User.query.get(user_id)
        return u
    except:
        return None

@app.route("/", methods=["GET"])
def landingPage():
    if(current_user.is_authenticated):
        return render_template("dashboard.html")
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST"])
def returningUser():
    user = User.query.filter_by(username=request.json['username']).first()
    if user is not None and user.check_password(request.json['password']):
        login_user(user)
        print("LOGGED IN USER WITH ID: " + str(user.id))
        return render_template("dashboard.html")
    else:
        return dict(msg = "FAILED")

@app.route("/dashboard", methods = ["GET"])
@login_required
def loadDashboard():
    return render_template("dashboard.html")

# @app.route("/browseclasses", method=["GET"])
# def loadClasses():


app.run()