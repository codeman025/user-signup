from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

    
def is_name(name):
    name, username_error = name, ""
    if name == "":
        username_error = "No username entered."
    elif len(name) < 3 or len(name) > 20:
        username_error = "Username must be between 3 and 20 characters long."
        name = ""
    elif " " in name:
        username_error = "There can be no spaces in the username."
        name = ""
    return name, username_error

def is_password(password):
    password, password_error = password, ""
    if password == "":
        password_error = "Enter a password"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters long."
        password = ""
    elif " " in password:
        password_error = "There can be no spaces in the password."
        password = ""
    return password, password_error

def is_valid(verify):
    verify, verify_error = verify, ""
    password = request.form['password']
    if password != "":
        if verify == "" or verify != password:
            verify_error = "Passwords do not match"
            verify = ""
            password = ""
    return verify, verify_error

def is_email(email):
    email, email_error = email, ""
    if email != "":
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters long."
            email = ""
        elif " " in email:
            email_error = "There can be no spaces in the email address."
            email = ""
        elif email.count("@") != 1 or email.count(".") != 1:
            email_error = "invalid email."
    return email, email_error



@app.route("/")
def login():
    return render_template('login.html')


@app.route("/validate", methods=['POST'])
def register():

    name, username_error = is_name(request.form["name"])
    password, password_error = is_password(request.form["password"])
    verify, verify_error = is_valid(request.form["verify"])
    email, email_error = is_email(request.form["email"])

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', name = name)
    else:
        return render_template('login.html', name = name, username_error = username_error, password_error = password_error, 
        verify_error = verify_error, email = email, email_error = email_error)
        

@app.route("/welcome", methods=['POST'])
def welcome():
    name = request.form['name']
    return render_template('welcome.html', title = "welcome", name = name)


app.run()