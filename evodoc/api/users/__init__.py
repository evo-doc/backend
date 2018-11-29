from evodoc.api.users.get_all import get_all
from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException

users = Blueprint('users', __name__, url_prefix='/users')


@users.errorhandler(EvoDocException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    'get_all',
    '__response_err',
]
