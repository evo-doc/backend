from evodoc.models import Module, Project
# from flask import g
from evodoc.exception import DbException, ApiException
import evodoc.conf as conf
import re
from evodoc import app


def create(g):
    """
    Creates module
        :param g: context
    """
    invalid = []
    g.project = Project.query.get_active(g.data['project'])
    if g.project is None:
        raise ApiException(
            404,
            "Project not found.",
            ['project'])

    if g.project.owner_id != g.token.user_id:
        contributor = 0
        for user in g.project.contributors:
            if user.id == g.token.user_id:
                contributor = 1
                break
        if contributor == 0:
            raise ApiException(
                403,
                "Access denied (no rights)",
                ['project'])

    if (not re.match('^[A-z0-9\_\-\ ]{2,}$', g.data['name'].strip()) or  # noqa W605
        Module.query.filter_by(project_id=g.project.id,
                               name=g.data['name']).first()
        is not None):
        invalid.append("name")

    if ((not isinstance(g.data['dependency'], list))and
            g.data['dependency'] != 'independent'):
        invalid.append("dependency")

    if 'body' not in g.data['content']:
        invalid.append("content")

    if invalid != []:
        raise ApiException(
            400,
            "Module data are invalid or non-unique.",
            invalid)

    g.module = Module(g.data['name'], g.data['description'],
                      g.project.id, g.token.user_id)

    if g.data['dependency'] != 'independent':
        for each in g.data['dependency']:
            dependency = Module.query.filter_by(
                project_id=g.project.id, name=each).first()
            if (dependency is None) or (dependency in g.module.dependencies):
                raise DbException(
                    400,
                    "Module data are invalid or non-unique.",
                    ['dependency'])
            g.module.dependencies.append(dependency)

    if 'type' in g.data['content']:
        g.module.contentType = g.data['content']['type']

    app.db.session.add(g.module)
    app.db.session.commit()

    with open(conf.FILE_PATH +
              '/' +
              str(g.project.id) +
              '/' +
              str(g.module.id) +
              '.txt', 'w+') as file:
        file.write(str(g.data['content']['body']))
