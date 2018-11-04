from evodoc.services.authorisation import login
from evodoc.api.tools import response_ok
from evodoc.api.auth import auth
from evodoc.services.decorators import ValidateData


@auth.route('/signin', methods=['POST'])
@ValidateData(["login", "password"])
def signIn():
    return response_ok(login())
