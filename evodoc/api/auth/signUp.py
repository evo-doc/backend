from evodoc.services.authorisation import register
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateData
from flask import g


@auth.route('/signup', methods=['POST'])
@ValidateData(["email", "password", "username"])
def signUp():
    register()
    return response_ok({"token": g.token.token, "username": g.user.name})
