from evodoc.services.authorisation import register
from flask import request
from evodoc.api.tools import response_ok, validate_data
from evodoc.api.auth import auth
from evodoc.exception import ApiException


@auth.route('/signup', methods=['POST'])
def signUp():
    data = request.get_json()
    validate_data(data, ["email", "password", "username"])
    return response_ok(
        register(data["username"], data["email"], data["password"]))
