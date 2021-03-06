from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException


projects = Blueprint('projects', __name__, url_prefix='/projects')


from evodoc.api.projects.create import api_create  # noqa F402
from evodoc.api.projects.view import api_view, api_view_modules  # noqa F402
from evodoc.api.projects.patch import api_patch  # noqa F402
from evodoc.api.projects.delete import api_delete  # noqa F402
from evodoc.api.projects.addContributor import api_addContributor  # noqa F402
from evodoc.api.projects.rmContributor import api_rmContributor  # noqa F402


@projects.errorhandler(EvoDocException)
def __response_err(data):
    """
    Error handler for EvoDocExceptions
        :param data: Exception data
    """
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    "projects",
    "api_create",
    "api_view",
    "api_view_modules",
    "api_patch",
    "api_delete",
    "api_addContributor",
    "api_rmContributor",
    "__response_err",
]
