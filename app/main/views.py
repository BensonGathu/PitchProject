from flask import render_template
from . import main
from flask_login import login_required
from .forms import UpdateProfileForm,PitchUploadForm,CommentsForm
from .. import db

#Views
@main.route("/",methods = ['GET','POST'])
def index():
    title = "Lets get Pitched"
    return render_template("index.html",title=title)

@main.route("/pitch")
def pitch():
    pitches = Pitch.query.filter_by().first()

    return render_template("pitch.html",pitches=pitches) 