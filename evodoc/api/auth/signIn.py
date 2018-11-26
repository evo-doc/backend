from evodoc.services.authorisation import login
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateData
from flask import g


@auth.route('/signin', methods=['POST'])
@ValidateData(["login", "password"])
def signIn():
    login()
    return response_ok({
        "token": g.token.token,
        "username": g.user.name
    })
