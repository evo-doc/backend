from evodoc.services.authorisation import login
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateData
# from flask import g
from evodoc.services.decorators import CreateContext


@auth.route('/signin', methods=['POST'])
@CreateContext()
@ValidateData(["login", "password"])
def signIn(g):
    login(g)
    return response_ok({
        "token": g.token.token,
        "username": g.user.name
    })
