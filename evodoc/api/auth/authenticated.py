from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateToken
from evodoc.services.decorators import CreateContext


@auth.route('/authenticated', methods=['GET'])
@CreateContext()
@ValidateToken()
def authenticated(g):
    return response_ok({
        "message": "User is authenticated."
    })
