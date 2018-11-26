from evodoc.models import Project
from flask import g
from evodoc.exception import DbException


def view():
    aProject = Project.query.get_or(g.id)

    if aProject is None:
        raise DbException(400,
                          "Project data are invalid or non-unique.",
                          invalid=['id'])
    return aProject
