from flask import Blueprint, render_template, session

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def homepage():
    if "current_user" in session:
        name = session["current_user"]["firstname"]
        logged_in = True
    else:
        name = None
        logged_in = False
    return render_template("index.html", logged_in=logged_in, name=name)
