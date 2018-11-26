from evodoc.models import Project, User
from flask import g
from evodoc import app
from evodoc.exception.dbException import DbException


def addContributor():
    g.project = Project.query.get_or(g.id)
    if g.project is None:
        raise DbException(404,
                          "Project not found.",  # noqa W605
                          invalid=['id'])

    if g.project.owner_id != g.token.user_id:
        raise DbException(403, "Access denied (no rights)")

    g.project.contributors.append(User.query.getByName(g.data['username']))

    app.db.session.merge(g.project)
    app.db.session.flush()
    app.db.session.commit()
