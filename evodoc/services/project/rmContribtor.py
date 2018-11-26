from evodoc.models import Project, User
from flask import g
from evodoc import app
from evodoc.exception.dbException import DbException


def rmContributor():
    g.project = Project.query.get_or(g.id)
    if g.project is None:
        raise DbException(404,
                          "Project project not found.",  # noqa W605
                          invalid=['id'])

    if g.project.owner_id != g.token.user_id:
        raise DbException(403, "Access denied (no rights)")

    user = User.query.getByName(g.data['username'])

    if user in g.project.contributors:
        g.project.contributors.remove(User.query.getByName(g.data['username']))

        app.db.session.merge(g.project)
        app.db.session.flush()
        app.db.session.commit()
