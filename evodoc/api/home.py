from evodoc.api.tools import response_ok
from evodoc.services.decorators import ValidateToken
from evodoc.services.stats import get_stats
from evodoc.exception import EvoDocException
from flask import Blueprint, jsonify
from evodoc.services.decorators import CreateContext

homeprint = Blueprint("home", __name__)


@homeprint.errorhandler(EvoDocException)
def __response_err(data):
    return jsonify({
        "message": data.message,
        "invalid": data.invalid
    }), data.errorCode


@homeprint.route('/')
@CreateContext()
def home(g):
    return jsonify("Hello there")


@homeprint.route('/stats/common')
@CreateContext()
@ValidateToken()
def stats(g):
    return response_ok(get_stats(g))
