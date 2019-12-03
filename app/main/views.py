from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required, current_user

# Views
@main.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')