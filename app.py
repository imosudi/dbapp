import os
import sys
from flask import Flask, render_template, redirect, request, session, flash

#Running my current job
from flask_mysqldb import MySQL


from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_moment import Moment
from datetime import datetime
#from flask_script import Manager
from flask_wtf import FlaskForm

from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField, IntegerField, HiddenField
from wtforms.validators import Required

from passlib.hash import sha256_crypt


#Create application
app = Flask(__name__)  
app.config['SECRET_KEY'] = 'This is really hard to guess string'  
  
bootstrap = Bootstrap(app)  
moment = Moment(app)  
admin = Admin(app)  
#manager = Manager(app)  


                     
"""
python
from noteapp import db
db.create_all()
"""

from models import *
import config


#Config MySQL
app.config['MYSQL_USER'] = 'sql2366691'
app.config['MYSQL_PASSWORD'] = 'lD9%zU9%'
app.config['MYSQL_HOST'] = 'sql2.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql2366691'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)




@app.route("/")
def home():
    pageName = "home"
    return render_template("home.html", pageName=pageName, current_time=datetime.utcnow())


@app.route("/notes/create", methods=["GET", "POST"])  
def create_note():
    pageName = "/notes/create"
    if request.method == "GET":
        return render_template("create_note.html", pageName=pageName, current_time=datetime.utcnow())
    else:
        title = request.form["title"]
        body = request.form["body"]  
        note = Note(title=title, body=body)
        db.session.add(note)
        db.session.commit()
        return redirect("/notes/create", form=form, current_time=datetime.utcnow())

@app.route("/notes", methods=["GET", "POST"])  
def notes():
    pageName = "/notes"
    notes = Note.query.all()
    return render_template("notes.html", notes=notes, pageName=pageName, current_time=datetime.utcnow())



@app.route('/register', methods=['GET', 'POST'])
def register():
    pageName= "/register"
    form = registrationForm()
    #form2 = registrationForm()
    
    if request.method == 'POST': # and  form.validate():
       name = form.name.data
       username = form.username.data
       email = form.email.data
       password = sha256_crypt.encrypt(str(form.password.data))
       cur = mysql.connection.cursor()  
       print(name, username, email, password)     
       cur.execute('''INSERT INTO users(name, username, email, password) VALUES(%s, %s, %s, %s)''', (name, username, email, password))
	 
       mysql.connection.commit()
       flash(u"Registration Complete, you may proceed to login", "success")
    return render_template('register.html', form=form, pageName=pageName,  current_time=datetime.utcnow())



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG_MODE)
    #manager.run(

