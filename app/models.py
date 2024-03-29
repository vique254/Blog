from . import db
from flask_login import UserMixin,current_user
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    blogs = db.relationship('Blog',backref = 'user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'{self.username}'
    
class Quotes:
    def __init__(self,author,quote):
        self.author=author
        self.quote=quote
        
class Blog(db.Model): 
        __tablename__='blogs'
        id = db.Column(db.Integer, primary_key = True)
        username = db.Column(db.String(255))
        title = db.Column(db.String(255))
        blog = db.Column(db.Text)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        
        comments = db.relationship('Comment' , backref= 'blog', lazy='dynamic')
    
        def save_blog(self):
            db.session.add(self)
            db.session.commit()
        @classmethod
        def get_blogs(cls,category):
            blogs=Blog.query.filter_by(category=category).all()
            return blogs
        @classmethod
        def get_blog(cls,id):
            blog = Blog.query.filter_by(id=id).first()
            return blog
class Comment(db.Model):
        __tablename__  = 'comments'
        
        id = db.Column(db.Integer, primary_key = True)
        comment=db.Column(db.String(255))
        blog_id =db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
        
        def save_comment(self):
            db.session.add(self)
            db.session.commit()
        
        @classmethod
        def get_comments(cls,blog_id):
            comments = Comment.query.filter_by(blog_id=blog_id).all()
            return comments
                
   

