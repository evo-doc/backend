from flask import json, request, Blueprint, jsonify
from evodoc.exception import ApiException, DbException

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.errorhandler(ApiException)
@auth.errorhandler(DbException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


from evodoc.api.auth.signUp import signUp
from evodoc.api.auth.signIn import signIn
from evodoc.api.auth.signOut import signOut
from evodoc.api.auth.authenticated import authenticated
__all__ = [
    "signUp",
    "signIn",
    "signOut",
    "authenticated",
    "__response_err"
]
