from evodoc.models import User
from evodoc.exception import DbException, ApiException
from flask import g
import re
from evodoc import app


def update_user(data):
    user_up = g.token.user
    if ('username' in data
            and data['username'] is not None):
        user = User.query.getByName(data['username'], False)
        if user is not None:
            raise DbException(400,
                              "This username is already in use.",
                              ['username'])
        else:
            user_up.name = data['username']

    if ('email' in data
            and data['email'] is not None):
        if not re.match('[^@]+@[^@]+\.[^@]+', data["email"]):  # noqa W605
            raise ApiException(400, "Supplied email is not valid.", ['email'])
        user = User.query.getByEmail(data['email'], False)
        if user is not None:
            raise DbException(400,
                              "This email is already in use.",
                              ['email'])
        else:
            user_up.email = data['email']

    if ('name' in data and data['name'] is not None):
        user_up.fullname = data['name']

    app.db.session.flush()
    app.db.session.commit()

    return user_up
