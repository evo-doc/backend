from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException

users = Blueprint('users', __name__, url_prefix='/users')
user = Blueprint('user', __name__, url_prefix='/user')

from evodoc.api.users.api_users import *  # noqa F402


@users.errorhandler(EvoDocException)
@user.errorhandler(EvoDocException)
def __response_err(data):
    """
    Error handler for EvoDocExceptions
        :param data:
    """
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    'get_all',
    'get_account',
    '__response_err',
]
