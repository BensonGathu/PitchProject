from flask import render_template
from . import main

#Views
@main.route("/")
def index():
    title = "Lets get Pitched"
    return render_template("index.html",title=title)