from evodoc.models import Project
from flask import g
from evodoc import app
import re
from evodoc.exception.dbException import DbException


def patch():
    g.project = Project.query.get_or(g.id)
    if g.project is None:
        raise DbException(404,
                          "Project doesn't exist.",  # noqa W605
                          invalid=['id'])
    if ((g.data["name"] is not None) and  # noqa W605
            (not re.match('^[A-z0-9\_\-]{2,}$', g.data["name"]))):
        raise DbException(400,
                          "Project name is too short.",
                          invalid=['name'])

    if g.project.owner_id != g.token.user_id:
        raise DbException(403, "Access denied (no rights)")

    if g.data['name'] is not None:
        g.project.name = g.data['name']

    if g.data['description'] is not None:
        g.project.description = g.data['description']

    app.db.session.merge(g.project)
    app.db.session.flush()
    app.db.session.commit()
