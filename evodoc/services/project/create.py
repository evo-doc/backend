from evodoc.models import Project, User
from flask import g
from evodoc import app
import pathlib
import evodoc.conf as conf
import re
from evodoc.exception.dbException import DbException


def create():
    if (not re.match('^[A-z0-9\_\-\ ]{2,}$', g.data['name'].strip())):  # noqa W605
        raise DbException(400,
                          "Project name is too short.",
                          invalid=["name"])

    g.project = Project(g.data["name"], g.data["description"], g.token.user_id)

    pathlib.Path(conf.FILE_PATH + '/' + str(g.project.id) +
                 '/').mkdir(parents=True, exist_ok=True)
    if 'contributors' not in g.data["collaborators"]:
        raise DbException(400,
                          "Project data are invalid.",
                          invalid=["collaborators"])

    app.db.session.add(g.project)
    app.db.session.commit()

    for i in g.data["collaborators"]["contributors"]:
        g.project.contributors.append(User.query.getByName(i))

    app.db.session.merge(g.project)
    app.db.session.flush()
    app.db.session.commit()
