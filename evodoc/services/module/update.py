from evodoc.models import Module, Project
# from flask import g
from evodoc.exception import DbException, ApiException
from evodoc import app
import re
from evodoc.conf import FILE_PATH


def update(g):
    """
    Updates module by data provided in g.data
        :param g: context
    """
    invalid = []
    g.module = Module.query.get_active(g.id)
    if g.module is None:
        raise ApiException(
            404,
            "Module not found.",
            ['module'])

    g.project = Project.query.get_active(g.module.project_id)
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

    if 'name' in g.data:
        if ((not re.match('^[A-z0-9\_\-\ ]{2,}$', g.data['name'].strip())) or  # noqa W605
            Module.query.filter_by(
                project_id=g.project.id, name=g.data['name']).first()
            not in [None, g.module]):
            invalid.append("name")
        else:
            g.module.name = g.data['name']

    if 'description' in g.data:
        g.module.description = g.data['description']

    if 'dependency' in g.data:
        if ((not isinstance(g.data['dependency'], list)) and
                (g.data['dependency'] != 'independent')):
            invalid.append("dependency")
        if g.data['dependency'] == 'independent':
            g.module.dependencies = []
        else:
            for each in g.data['dependency']:
                flag = 0
                for x in g.module.dependencies:
                    if x.name == each:
                        flag = 1
                        break
                if flag == 0:
                    dependency = Module.query.filter_by(
                        project_id=g.project.id, name=each).first()
                    if ((dependency is None) or
                            (dependency in g.module.dependencies)):
                        invalid.append('dependency')
                        break
                    g.module.dependencies.append(dependency)
    if 'content' in g.data:
        if 'body' not in g.data['content']:
            invalid.append('content')
            raise DbException(
                400,
                "Module data are invalid or non-unique.",
                invalid)
        with open(FILE_PATH +
                  '/' +
                  str(g.project.id) +
                  '/' +
                  str(g.module.id) +
                  '.txt', 'w+') as file:
            file.write(str(g.data['content']['body']))
        if 'type' in g.data['content']:
            g.module.contentType = g.data['content']['type']

    if invalid != []:
        raise DbException(
            400,
            "Module data are invalid or non-unique.",
            invalid)

    app.db.session.merge(g.module)
    app.db.session.flush()
    app.db.session.commit()
