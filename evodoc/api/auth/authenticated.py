from evodoc.api.tools import response_ok, validate_token
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateToken
from flask import g


@auth.route('/authenticated', methods=['GET'])
@ValidateToken()
def authenticated():
    return response_ok({
        "message": "User is authenticated."
    })
