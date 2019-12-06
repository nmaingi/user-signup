from flask import Flask, request, redirect, render_template
import cgi
import os

app=Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/welcome")
def welcome_page():
    name=request.args.get('username')
    return render_template('welcome.html', username=name)

    

@app.route("/home", methods=["POST"])
def validate_logon():
    username=request.form['username']
    password=request.form['password']
    retype=request.form['password2']
    email=request.form['email']

    username_error=""
    password_error=""
    password2_error=""
    email_error=""
    blank=""


    if username==blank:
        username_error="give username"
    else:
        if len(username)<3 or len(username)>20:
            username_error="out of range"
        elif username.count(' ')>0:
            username_error="cannot have spaces"
        
    if password==blank:
        password_error="give password"
    else:
        if len(password)<3 or len(password)>20:
            password_error= "password out of range"
        elif password.count(' ')>0:
            password_error="cannot contain spaces"
    
    if retype==blank:
        password2_error="give password"
    else:
        if len(retype)<3 or len(retype)>20:
            password2_error="password out of range"
        elif retype.count(' ')>0:
            password2_error="cannot contain spaces"
    
    if retype!=password:
        password2_error="password did not match"
    
    if email!=blank:
        if email.count('@')!=1:
            email_error="enter valid email"
        elif email.count('.')!=1:
            email_error="enter valid email"
        elif len(email)<3 or len(email)>20:
            email_error="email out of range"
        elif email.count(' ')>0:
            email_error="cannot contain spaces"


    if not username_error and not password_error and not password2_error and not email_error:
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template("home.html", username=username,username_error=username_error,password_error=password_error,
        password2_error=password2_error,email=email,email_error=email_error) 

app.run()

