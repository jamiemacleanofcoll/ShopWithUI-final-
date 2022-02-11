from flask import session
from models.user import User


def add_user_to_session(user: User):
    session["current_user"] = {
        "username": user.username,
        "user_id": user.user_id,
        "role": str(user.role),
        "firstname": user.firstname,
        "lastname": user.lastname,
        "password": user.password,
        "date of birth": user.date_of_birth,
    }
