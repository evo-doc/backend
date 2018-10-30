from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException

auth = Blueprint('auth', __name__, url_prefix='/auth')

from evodoc.api.auth.authenticated import authenticated  # noqa F402
from evodoc.api.auth.signOut import signOut  # noqa F402
from evodoc.api.auth.signIn import signIn  # noqa F402
from evodoc.api.auth.signUp import signUp  # noqa F402


@auth.errorhandler(EvoDocException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    "auth",
    "signUp",
    "signIn",
    "signOut",
    "authenticated",
    "__response_err",
]
