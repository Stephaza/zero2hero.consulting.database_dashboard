from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models.user import User

#Create Blueprint
user = Blueprint('user', __name__)

#Log In route
@user.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            #save user in session
            session['user'] = user.username
            return 'Logged in'
        else:
            return 'Invalid username or password'
    return render_template('login.html')