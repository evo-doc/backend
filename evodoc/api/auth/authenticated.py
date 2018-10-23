from flask import request
from evodoc.api.tools import response_ok, validate_token
from evodoc.api.auth import auth

@auth.route('/authenticated', methods=['GET'])
def authenticated():
    header = request.headers.get('Authorization')
    if header:
        token = header.split(" ")[1]
    else:
        token = ''

    validate_token(token)
    return response_ok({
        "message": "User is authenticated."
    })
