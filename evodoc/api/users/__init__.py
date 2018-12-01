from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException

users = Blueprint('users', __name__, url_prefix='/users')

from evodoc.api.users.api_users import *  # noqa F402


@users.errorhandler(EvoDocException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    'get_all',
    'get_account',
    '__response_err',
]