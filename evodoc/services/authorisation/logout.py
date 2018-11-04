from evodoc.models import UserToken
from flask import g


def logout():
    g.token.deleteWithPrevious()
