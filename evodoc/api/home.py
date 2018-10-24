from flask import Blueprint, jsonify
from evodoc.api.tools import response_ok_obj

homeprint = Blueprint("home", __name__)

@homeprint.route('/')
def home():
    return jsonify("Hello there")

    