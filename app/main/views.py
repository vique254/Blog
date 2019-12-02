from flask import render_template,request,redirect,url_for
from . import main
from .forms import ReviewForm
from ..models import Review


# Views
@main.route('/')
def index():