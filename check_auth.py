from functools import wraps

from flask import redirect, session, url_for
from models.user import Role


def check_user():
    if "current_user" in session:
        return True
    else:
        return False


def check_admin():
    if check_user() and session["current_user"]["role"] == str(Role.ADMIN):
        return True
    else:
        return False


def authorization_required(func):
    @wraps(func)
    def check_authorization(*args, **kwargs):
        if check_user():
            return func(*args, **kwargs)
        else:
            return redirect(url_for("main_bp.homepage"))

    return check_authorization


def admin_rights_required(func):
    @wraps(func)
    def check_authorization(*args, **kwargs):
        if check_admin():
            return func(*args, **kwargs)
        else:
            return redirect(url_for("main_bp.homepage"))

    return check_authorization
