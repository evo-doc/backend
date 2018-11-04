from flask import jsonify
from evodoc.exception import ApiException
from evodoc.models import UserToken
from datetime import datetime


def serialize_list(l):
    """
    Serialize data in list, for each class in list calls its
    serialize method at the end return whole list of serialized values
        :param l: List of objects which have serialize method
    """
    return [m.serialize() for m in l]


def response_ok_obj(data):
    """
    Returns object on which is serialized as json response
        :param data: object with serialize method
    """
    return jsonify(data.serialize())


def response_ok(data):
    """
    Converts data to json format and return them as server response
        :param data:
    """
    return jsonify(data)


def response_ok_list(data):
    """
    Converts list to list of serialized values and then send them as
    json response
        :param data: list of objects with serialize method
    """
    return jsonify(serialize_list(data))


def validate_token(token):
    """
    Validate token and return its instance
        :param token:
    """
    t = UserToken.query.filter_by(token=token).first()
    if t is None:
        raise ApiException(
            401, "Unauthorised user (missing or outdated token)", ['token'])
    if t.update <= datetime.utcnow():
        t = UserToken.createSuccessor()
    return t.token


def validate_data(data, expected_values=[],
                  message="Not enough data to process the request.",
                  errorCode=422):
    """
    validate data by given array of keys
    """
    missing = []

    if data is None or data == {}:
        raise ApiException(422, "Not enough data to process the request.")
    for value in expected_values:
        if value not in data or data[value] is None or data[value] == {}:
            missing.append(value)

    if missing != []:
        raise ApiException(errorCode, message, missing)
