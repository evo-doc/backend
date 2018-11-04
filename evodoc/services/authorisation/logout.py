from flask import g


def logout():
    g.token.deleteWithPrevious()
