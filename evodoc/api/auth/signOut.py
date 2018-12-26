from evodoc.services.authorisation import logout
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateToken
from evodoc.services.decorators import CreateContext


@auth.route('/signout', methods=['GET'])
@CreateContext()
@ValidateToken()
def signOut(g):
    """
    Api method for user sign out
        :param g: context bearing user token
    """
    logout(g)
    return response_ok({
        "message": "User signed out."
    })
