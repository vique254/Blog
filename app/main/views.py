from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required, current_user
from ..request import get_quotes
from ..models import User

# Views
@main.route('/')
def index():
    quotes=get_quotes()
    return render_template('index.html',quotes=quotes)