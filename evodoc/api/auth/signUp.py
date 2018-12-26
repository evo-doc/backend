from evodoc.services.authorisation import register
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateData
# from flask import g
from evodoc.services.decorators import CreateContext


@auth.route('/signup', methods=['POST'])
@CreateContext()
@ValidateData(["email", "password", "username"])
def signUp(g):
    """
    Api method for user sign up
        :param g: Context bearing request data
    """
    register(g)
    return response_ok({"token": g.token.token, "username": g.user.name})
