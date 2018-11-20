from flask import Blueprint, jsonify
from evodoc.services import register

homeprint = Blueprint("home", __name__)


@homeprint.route('/')
def home():
    return jsonify("Hello there")
