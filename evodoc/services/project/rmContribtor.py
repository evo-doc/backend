from evodoc.models import Project, User
# from flask import g
from evodoc import app
from evodoc.exception.dbException import DbException


def rmContributor(g):
    """
    Removes project contributor
        :param g: context
    """
    g.project = Project.query.get_or(g.id)
    if g.project is None:
        raise DbException(404,
                          "Project not found.",  # noqa W605
                          invalid=['id'])

    if g.project.owner_id != g.token.user_id:
        raise DbException(403, "Access denied (no rights)")

    user = User.query.getByName(g.data['username'])

    if user in g.project.contributors:
        g.project.contributors.remove(user)

        app.db.session.merge(g.project)
        app.db.session.flush()
        app.db.session.commit()
    else:
        raise DbException(202, "This user is not a collaborator.")
