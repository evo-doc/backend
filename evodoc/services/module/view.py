from evodoc.models import Module, Project
# from flask import g
from evodoc.exception import ApiException


def view(g):
    """
    Saves instance of module to g
        :param g: context
    """
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
