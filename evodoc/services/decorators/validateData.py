from flask import request
from evodoc.exception import ApiException


class ValidateData(object):
    def __init__(self, expected_values):
        self.expected_values = expected_values

    def __call__(self, f):
        def wrapper(g, *args, **kwargs):
            missing = []
            g.data = request.get_json()

            if g.data is None or g.data == {}:
                raise ApiException(
                    422, "Not enough data to process the request.")
            for value in self.expected_values:
                if (value not in g.data or
                    g.data[value] is None or
                        g.data[value] == {}):
                    missing.append(value)

            if missing != []:
                raise ApiException(
                    422,
                    "Not enough data to process the request.",
                    missing)
            return f(g, *args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
