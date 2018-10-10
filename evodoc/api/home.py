from flask import Blueprint, jsonify

homeprint = Blueprint("home", __name__)

@homeprint.route('/')
def home():
    return jsonify("Hello there")