from evodoc.services.authorisation import login
from flask import request
from evodoc.api.tools import response_ok, validate_data
from evodoc.api.auth import auth

@auth.route('/signin', methods=['POST'])
def signIn():
    data = request.get_json()
    validate_data(data,["login", "password"], message="Sign in data are invalid.")
    return response_ok(login(data["login"],data["password"]))
