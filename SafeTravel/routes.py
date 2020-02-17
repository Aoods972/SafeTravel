from flask import render_template, url_for, flash, redirect, request
from SafeTravel.forms import SignUpForm, LoginForm
from SafeTravel import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from SafeTravel.models import User

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Implement login functionality
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Implement signup functionality
    return render_template("signup.html")

@app.route("/home")
def userpage():
    return render_template("userpage.html")