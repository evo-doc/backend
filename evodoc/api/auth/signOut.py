from evodoc.services.authorisation import logout
from flask import request
from evodoc.api.tools import response_ok, validate_token
from evodoc.api.auth import auth

@auth.route('/signout', methods=['GET'])
def signOut():
    header = request.headers.get('Authorization')
    if header:
        token = header.split(" ")[1]
    else:
        token = ''

    validate_token(token)
    logout(token)
    return response_ok({
        "message": "User signed out."
    })