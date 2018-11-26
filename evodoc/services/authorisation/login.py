from evodoc.models import User
from evodoc.exception import ApiException
from flask import g


def login():
    g.user = User.query.getByNameOrEmail(g.data["login"])

    if g.user is None or g.user.password != g.data["password"]:  # TBA
        raise ApiException(400, "Sign in data are invalid.")

    g.token = g.user.createToken()
