from evodoc.api.tools import response_ok_obj, response_ok_list
from evodoc.api.projects import projects
from evodoc.services.project import view, view_modules
from evodoc.services.decorators import ValidateToken
# from flask import g
from evodoc.services.decorators import CreateContext


@projects.route('/<int:id>', methods=['GET'])
@CreateContext()
@ValidateToken()
def api_view(g, id):
    """
    Api method for viewing project
        :param g: context
        :param id: module id
    """
    g.id = id
    view(g)
    return response_ok_obj(g.project)


@projects.route('/<int:id>/modules', methods=['GET'])
@CreateContext()
@ValidateToken()
def api_view_modules(g, id):
    """
    Api method for listing project modules
        :param g: context
        :param id: module id
    """
    g.id = id
    return response_ok_list(view_modules(g))
