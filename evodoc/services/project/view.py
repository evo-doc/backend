from evodoc.models import Project
from flask import g
from evodoc.exception import DbException


def view():
    g.project = Project.query.get_or(g.id)

    if g.project is None:
        raise DbException(400,
                          "Project data are invalid or non-unique.",
                          invalid=['id'])
