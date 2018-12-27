from evodoc.models import Module, Project
# from flask import g
from evodoc import app
from evodoc.exception import ApiException
import datetime


def module_delete(g):
    """
    Module deletion
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

    # for each in app.db.session.query(ModuleDependencies).filter_by(
    #       used_in_module_id=g.module.id).all():
    #     module=Module.query.get_active(each.dependency_id)
    #     if(module is not None):
    #         raise ApiException(
    #             400,
    #             "Module can not be deleted.",
    #             ['dependency'])

    g.module.delete = datetime.datetime.utcnow()

    app.db.session.merge(g.module)
    app.db.session.flush()
    app.db.session.commit()
