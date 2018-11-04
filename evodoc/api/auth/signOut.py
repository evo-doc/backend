from evodoc.services.authorisation import logout
from evodoc.api.tools import response_ok, validate_token
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateToken
from flask import g


@auth.route('/signout', methods=['GET'])
@ValidateToken()
def signOut():
    logout()
    return response_ok({
        "message": "User signed out."
    })
