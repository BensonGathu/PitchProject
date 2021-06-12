from flask import render_template
from app import app

#Views
@app.route("/")
def index():
    title = "Lets get Pitched"
    return render_template("index.html",title=title)