from flask import request
from evodoc.models import UserToken
from datetime import datetime
from evodoc.exception import ApiException


class ValidateToken(object):
    """
    Token validator (function wrapper)
    Checks if token is provided in request header, and if its valid.
    If it is saves instance of token to context (g) if not raises exception.
    """

    def __call__(self, f):
        def wrapper(g, *args, **kwargs):
            header = request.headers.get('Authorization')
            if header and 'Bearer ' in header:
                token = header.split(" ")[1]
            else:
                token = ''

            tokenObject = UserToken.query.filter_by(token=token).first()
            if tokenObject is None:
                raise ApiException(
                    401,
                    "Unauthorised user (missing or outdated token)",
                    ['token'])
            if tokenObject.update <= datetime.utcnow():
                tokenObject = tokenObject.createSuccessor()
            g.token = tokenObject
            return f(g, *args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
