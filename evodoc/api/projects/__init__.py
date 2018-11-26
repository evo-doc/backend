from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException


projects = Blueprint('projects', __name__, url_prefix='/projects')


from evodoc.api.projects.create import api_create  # noqa F402
from evodoc.api.projects.view import api_view  # noqa F402


@projects.errorhandler(EvoDocException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    "projects",
    "api_create",
    "api_view",
    "__response_err",
]
