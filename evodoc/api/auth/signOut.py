from evodoc.services.authorisation import logout
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateToken


@auth.route('/signout', methods=['GET'])
@ValidateToken()
def signOut():
    logout()
    return response_ok({
        "message": "User signed out."
    })
