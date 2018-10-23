from flask import Blueprint, jsonify
from evodoc.services.authorisation import register
from evodoc.api.tools import response_ok_obj

homeprint = Blueprint("home", __name__)


@homeprint.route('/')
def home():
    return jsonify("Hello there")

@homeprint.route('/test')
def test():
    return register("kek","kek2@kek.kek","kek").serialize()
