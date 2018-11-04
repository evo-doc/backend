from evodoc.models import User
from evodoc.exception import ApiException
from flask import g


def login():
    user = User.query.getByNameOrEmail(g.data["login"])

    if user is None or user.password != g.data["password"]:  # TBA
        raise ApiException(400, "Sign in data are invalid.")

    return {"token": user.createToken().token, "username": user.name}
