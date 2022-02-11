from controllers.user_controller import UserController
from flask import Blueprint, redirect, render_template, request, session, url_for

from views.user_helper import add_user_to_session

from .check_auth import authorization_required, check_user

user_bp = Blueprint("user_bp", __name__)

user_controller = UserController()


@user_bp.route("/", methods=["GET"])
@authorization_required
def profile():
    return render_template(
        "profile.html", user_dict=session["current_user"], logged_in=check_user()
    )


@user_bp.route("/", methods=["POST"])
@authorization_required
def profile_submit():
    return redirect(url_for("user_bp.edit_profile"))


@user_bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@user_bp.route("/login", methods=["POST"])
def login_submit():
    data = request.form
    if user_controller.login(username=data["username"], password=data["password"]):
        add_user_to_session(user_controller.view_account())
        return redirect(url_for("main_bp.homepage"))
    else:
        return redirect(url_for("user_bp.login"))


@user_bp.route("/logout", methods=["GET"])
@authorization_required
def logout():
    session.pop("current_user")
    user_controller.logout()
    return redirect(url_for("main_bp.homepage"))


@user_bp.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")


@user_bp.route("/signup", methods=["POST"])
def signup_submit():
    data = request.form
    user_controller.create_user(
        firstname=data["firstname"],
        lastname=data["lastname"],
        date_of_birth=data["date of birth"],
        username=data["username"],
        password=data["password"],
    )
    user_controller.login(username=data["username"], password=data["password"])
    user = user_controller.view_account()
    add_user_to_session(user)
    return redirect(url_for("main_bp.homepage"))


@user_bp.route("/edit_profile", methods=["GET"])
@authorization_required
def edit_profile():
    # exclude role attribute
    user_dict = {
        attribute: session["current_user"][attribute]
        for attribute in session["current_user"]
        if attribute != "role" and attribute != "user_id"
    }
    return render_template(
        "profile.html", user_dict=user_dict, edit=True, logged_in=check_user()
    )


@user_bp.route("/edit_profile", methods=["POST"])
@authorization_required
def edit_profile_submit():
    data = dict(request.form)

    for attribute, value in data.items():
        user_controller.change_attribute(attribute, value)

    user = user_controller.view_account()
    add_user_to_session(user)
    return redirect(url_for("user_bp.profile"))
