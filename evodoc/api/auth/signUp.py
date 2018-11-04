from evodoc.services.authorisation import register
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateData


@auth.route('/signup', methods=['POST'])
@ValidateData(["email", "password", "username"])
def signUp():
    return response_ok(
        register())
