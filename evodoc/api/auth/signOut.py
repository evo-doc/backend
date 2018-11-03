from evodoc.services.authorisation import logout
from evodoc.api.tools import response_ok, validate_token
from evodoc.api.auth import auth
from evodoc.services.decorators import getToken


@auth.route('/signout', methods=['GET'])
@getToken
def signOut(token):
    validate_token(token)
    logout(token)
    return response_ok({
        "message": "User signed out."
    })
