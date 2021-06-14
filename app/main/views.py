from flask import render_template,request,redirect,url_for,abort
from .. models import Pitch,Comment,User,UpVotes,DownVotes
from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfileForm,PitchUploadForm,CommentsForm
from .. import db,photos


#Views
@main.route("/",methods = ['GET','POST'])
def index():
    title = "Lets get Pitched"
    pitches = Pitch.query.filter_by().all()
    return render_template("index.html",title=title,pitches=pitches)

@main.route("/pitch")
def pitch():
    pitches = Pitch.query.filter_by().first()

    return render_template("pitch.html",pitches=pitches) 


@main.route("/user/<uname>")
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches = Pitch.query.filter_by(user_id=current_user.id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches=pitches)


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



    return render_template('new_pitch.html', form=form)


@main.route('/user/<name>/upload_pitch', methods = ['POST','GET'])
@login_required
def new_pitch(name):
    user = User.query.filter_by(username = name).first()
    form = PitchUploadForm()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(pitch=pitch,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()
        return redirect(url_for('main.index', form = form))
    return render_template('new_pitch.html', form = form)