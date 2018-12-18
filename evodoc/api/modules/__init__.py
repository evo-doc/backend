from flask import Blueprint, jsonify
from evodoc.exception import EvoDocException


modules = Blueprint('modules', __name__, url_prefix='/modules')


from evodoc.api.modules.create import api_create  # noqa F402
from evodoc.api.modules.view import api_view  # noqa F402
from evodoc.api.modules.build import api_build  # noqa F402
from evodoc.api.modules.update import api_update  # noqa F402
from evodoc.api.modules.delete import api_delete  # noqa F402


@modules.errorhandler(EvoDocException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


__all__ = [
    "modules",
    "api_create",
    "api_view",
    "api_build",
    "api_patch",
    "api_delete",
    "__response_err",
]
