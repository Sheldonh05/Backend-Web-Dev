from flask import Blueprint

auth = Blueprint("auth",__name__)

### decorators to create routes or pages of website
@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/logout")
def Logout():
    return "<p>Logout</p>"

@auth.route("/sign-up")
def sign_up():
    return "<p>Sign-up</p>"
