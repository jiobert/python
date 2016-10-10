
from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
import re
mysql = MySQLConnector(app,'email_validation_with_db')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
    if not 'class' in session:
        session['class'] = ''
    if not 'form' in session:
        session['form'] = 'show'
    if not 'database' in session:
        session['database'] = 'hide'
    query = "SELECT * FROM user"                           # define your query
    addresses = mysql.query_db(query)
    print addresses
    return render_template('index.html', all_addresses=addresses)

@app.route('/process', methods=['POST'])
def add_email():
    if len(request.form['email']) <1:
        flash('Enter email address.')
        session['class'] = 'red'

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address.')
        session['class'] = 'red'

    else:
        print request.form['email']

        query = "INSERT INTO user (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
                 'email': request.form['email']
               }
        mysql.query_db(query,data)

        flash('The email address you entered ({}) is a VALID email address!  Thank you!'.format(request.form['email']))
        session['class'] = 'green'
        session['form'] = 'hide'
        session['database'] = 'show'

    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
