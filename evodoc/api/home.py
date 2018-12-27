from evodoc.api.tools import response_ok
from evodoc.services.decorators import ValidateToken
from evodoc.services.stats import get_stats
from evodoc.exception import EvoDocException
from flask import Blueprint, jsonify
from evodoc.services.decorators import CreateContext

homeprint = Blueprint("home", __name__)


@homeprint.errorhandler(EvoDocException)
def __response_err(data):
    """
    Error handler
        :param data: exception data
    """
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


@homeprint.route('/')
@CreateContext()
def home(g):
    """
    Home api method for testing purposes
        :param g: context
    """
    return jsonify("Hello there")


@homeprint.route('/stats/common')
@CreateContext()
@ValidateToken()
def stats(g):
    """
    Api method for listing statistics
        :param g: context
    """
    return response_ok(get_stats(g))
