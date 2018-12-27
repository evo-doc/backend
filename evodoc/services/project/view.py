from evodoc.models import Project
# from flask import g
from evodoc.exception import DbException


def view(g):
    g.project = Project.query.get_active(g.id)

    if g.project is None:
        raise DbException(404,
                          "Project doesn't exist.",
                          invalid=['id'])


def view_modules(g):
    project = Project.query.filter(
        Project.id == g.id, Project.delete.is_(None)).first()

    if project is None:
        raise DbException(400,
                          "Project does not exist.",
                          invalid=['id'])

    return project.modules
