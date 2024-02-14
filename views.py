from flask import Blueprint

views = Blueprint('views',__name__)

#the view of the page in the route
@views.route('/')
def home():
    return "<h1>Test</h1>"

