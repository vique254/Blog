from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required, current_user
from ..request import get_quotes
from ..models import User, Blog,Comment
from .forms import BlogForm,UpdateProfile,CommentForm
from .. import db,photos



# Views
@main.route('/')
def index():
    quotes=get_quotes()
    blogs = Blog.query.all()
    print(blogs)
    comments =Comment.query.all()
    print(comments)
    return render_template('index.html', quotes=quotes, blogs=blogs, comments=comments)

@main.route('/profile/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)
    
@main.route('/blog/new/', methods = ['GET','POST'])
@login_required  
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog = blog_form.blog.data
        title = blog_form.title.data
        username=blog_form.username.data
        print(current_user._get_current_object().id)
        new_blog = Blog(title = title,blog=blog,username=current_user)
        db.session.add(new_blog)
        db.session.commit()
        
        print(new_blog.blog)
        print(new_blog.title)
        
        return redirect(url_for('main.index'))
    
    return render_template('new_blog.html', blog_form = blog_form)

@main.route('/blog/comment/<int:id>', methods = ['GET','POST'])
def comment(id):
    blog = Blog.get_blog(id)
    comment_form = CommentForm()
    comments = Comment.get_comments(id)
    if comment_form.validate_on_submit():
        comment = comment_form.description.data
        new_comment = Comment(comment=comment, blog_id = blog.id)
        new_comment.save_comment()
        print(new_comment.comment)
        print(new_comment.blog_id)
        return redirect(url_for("main.index",id=id))
    return render_template('comments.html',comment_form=comment_form,comments=comments)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    
    
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

        form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)