from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Length,DataRequired
from flask_wtf.file import FileField,file_allowed

class UpdateProfileForm(FlaskForm):
    bio = TextAreaField("More about you",validators=[Required()])
    submit = SubmitField("Submit")

class PitchUploadForm(FlaskForm):
    title = StringField("Title")
    category = SelectField('Choose category: ',validators=[DataRequired()],choices=[('Interview Pitch','Interview Pitch'),('Products Pitch','Products Pitch'),('IT World Pitch','IT World Pitch'),('Political Pitch','Political Pitch'),('Pickup Lines','Pickup Lines')])
    pitch = TextAreaField("Your Pitch",validators=[DataRequired()])
    submit = SubmitField("Post Pitch")

class CommentsForm(FlaskForm):
    comment = TextAreaField("Comment",validators=[DataRequired()])
    submit = SubmitField("Post Comment")
