from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateToken


@auth.route('/authenticated', methods=['GET'])
@ValidateToken()
def authenticated():
    return response_ok({
        "message": "User is authenticated."
    })
