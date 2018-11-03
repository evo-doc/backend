from evodoc.api.tools import response_ok, validate_token
from evodoc.api.auth import auth
from evodoc.services.decorators import getToken


@auth.route('/authenticated', methods=['GET'])
@getToken
def authenticated(token):
    validate_token(token)
    return response_ok({
        "message": "User is authenticated."
    })
