"""
Server: sql2.freemysqlhosting.net
Name: sql2366691
Username: sql2366691
Password: lD9%zU9%
Port number: 3306
"""

import os
import sys
from flask import Flask, render_template, redirect, request, session

#Running my current job
from flask_mysqldb import MySQL

import config

#Create application
app = Flask(__name__) 


#Config MySQL
app.config['MYSQL_USER'] = 'sql2366691'
app.config['MYSQL_PASSWORD'] = 'lD9%zU9%'
app.config['MYSQL_HOST'] = 'sql2.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql2366691'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


@app.route("/")
def index():
    cur = mysql.connection.cursor()
    """cur.execute(''' CREATE TABLE users ( 
	id INT(50) NOT NULL AUTO_INCREMENT , 
	email VARCHAR(150) NULL DEFAULT NULL , 
	name VARCHAR(150) NULL DEFAULT NULL , 
	username VARCHAR(150) NULL DEFAULT NULL , 
	password VARCHAR(150) NULL DEFAULT NULL , 
	INDEX (id)) ENGINE = InnoDB;
    ''')
    """
    #cur.execute(
    '''
    INSERT INTO users(name, username, email, password) VALUES('MOs Is', 'mosudi', 'mosudi@gmail.com', 'password')
    '''
    #)
    #cur.execute(
    '''
    INSERT INTO users(name, username, email, password) VALUES('MOs Isiaka', 'mosud', 'mimosudi@gmail.com', 'password')
    '''
    #)
    cur.execute(
    '''
    SELECT * FROM users
    '''
    )
    results = cur.fetchall()
    print(results)
    mysql.connection.commit()
    return 'Data Insert Done!'










if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG_MODE)
    #manager.run(

