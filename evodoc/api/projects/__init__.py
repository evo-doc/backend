from evodoc.api.projects import create
from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException

projects = Blueprint('projects', __name__, url_prefix='/projects')


@projects.errorhandler(EvoDocException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    "projects",
    "create",
    "__response_err",
]
