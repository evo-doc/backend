from evodoc.services.decorators import simple_decorator
from flask import request


@simple_decorator
def getToken(func):
    def decoratorFunction(*args, **kwargs):
        header = request.headers.get('Authorization')
        if header and 'Bearer ' in header:
            token = header.split(" ")[1]
        else:
            token = ''
        return func(token, *args, **kwargs)
    return decoratorFunction
