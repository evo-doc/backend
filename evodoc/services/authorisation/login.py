from evodoc.models import User
from evodoc.exception import ApiException
# from flask import g
from evodoc import app


def login(g):
    """
    User login
        :param g: context
    """
    g.user = User.query.getByNameOrEmail(g.data["login"])

    if g.user is None\
        or not app.bcrypt.check_password_hash(g.user.password,
                                              g.data['password']):
        raise ApiException(400, "Sign in data are invalid.")

    g.token = g.user.createToken()
