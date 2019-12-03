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

@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_blog = Blog(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))