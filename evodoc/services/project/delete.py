from evodoc.models import Project
# from flask import g
from evodoc import app
from evodoc.exception.dbException import DbException
import datetime


def project_delete(g):
    """
    Deletes project
        :param g: context
    """
    g.project = Project.query.get_active(g.id)

    if g.project is None:
        raise DbException(404,
                          "Project doesn't exist.",  # noqa W605
                          invalid=['id'])

    if g.project.owner_id != g.token.user_id:
        raise DbException(403, "Access denied (no rights)")

    g.project.delete = datetime.datetime.utcnow()

    app.db.session.merge(g.project)
    app.db.session.flush()
    app.db.session.commit()
