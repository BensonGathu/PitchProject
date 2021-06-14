from flask import render_template,request,redirect,url_for,abort
from .. models import Pitch,Comment,User,Votes,Category
from . import main
from flask_login import login_required
from .forms import UpdateProfileForm,PitchUploadForm,CommentsForm
from .. import db,photos

#Views
@main.route("/",methods = ['GET','POST'])
def index():
    title = "Lets get Pitched"
    return render_template("index.html",title=title)

@main.route("/pitch")
def pitch():
    pitches = Pitch.query.filter_by().first()

    return render_template("pitch.html",pitches=pitches) 

@main.route("/user/<uname>")
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfileForm()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

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
