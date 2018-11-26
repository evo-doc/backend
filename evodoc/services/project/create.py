from evodoc.models import Project, User
from flask import g
from evodoc import app
import pathlib
import evodoc.conf as conf
import re
from evodoc.exception.dbException import DbException


def create():
    invalid = []
    if (not re.match('^[A-z0-9\_\-]{2,}$', g.data["name"]) or  # noqa W605
            Project.query.getByName(g.data["name"], False) is not None):
        invalid.append("name")

    if invalid != []:
        raise DbException(400,
                          "Project data are invalid or non-unique.",
                          invalid=invalid)

    aProject = Project(g.data["name"], g.data["description"], g.token.user_id)
    app.db.session.add(aProject)
    app.db.session.commit()
    pathlib.Path(conf.FILE_PATH + '/' + str(aProject.id) +
                 '/').mkdir(parents=True, exist_ok=True)
    for i in g.data["collaborators"]["contributors"]:
        aProject.contributors.append(User.query.getByName(i))

    app.db.session.merge(aProject)
    app.db.session.flush()
    app.db.session.commit()
    return aProject
