# Importing required modules
from flask import session
from flask_session import Session
from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv

load_dotenv()
 
# Creating Flask App
app = Flask(__name__)
# Setting up Secret Key for Session Management
app.secret_key = "SECRET_KEY"
 
# Configuring Session
app.config['PERMANENT_SESSION_LIFETIME'] = 60  # Session Lifetime
app.config['SESSION_TYPE'] = "filesystem"  # Session Storage Type
 
# Path to Storing Session
app.config['SESSION_FILE_DIR'] = "session_data"

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

# Route for Registering Username
@app.route("/add", methods=["GET", "POST"])
def add_username():
    session['message'] = "Enter your username to continue."
    if request.method == 'POST':
        username = request.form['username']
        session['user'] = username
        session['greet'] = f"Successfully registered username - {session['user']}."
        return redirect(url_for("home"))
 
    return render_template("add_username.html")

# Route for Removing Username
@app.route("/remove")
def remove_username():
    session.pop('user')
    session['notify'] = "Username Removed from Session Storage."
    return redirect(url_for("home"))
 
# Initializing the Session Extension
Session(app)
 
# Remaining Code 