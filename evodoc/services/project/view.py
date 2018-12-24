from evodoc.models import Project
# from flask import g
from evodoc.exception import DbException


def view(g):
    g.project = Project.query.get_active(g.id)

    if g.project is None:
        raise DbException(404,
                          "Project doesn't exists.",
                          invalid=['id'])


def view_modules(g):
    project = Project.query.filter(Project.id == g.id).first()

    if project is None:
        raise DbException(400,
                          "Project does not exists.",
                          invalid=['id'])

    return project.modules
