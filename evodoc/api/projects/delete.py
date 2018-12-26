from evodoc.api.tools import response_ok
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateToken
from evodoc.services.project import project_delete
# from flask import g
from evodoc.services.decorators import CreateContext


@projects.route('/<int:id>', methods=['DELETE'])
@CreateContext()
@ValidateToken()
def api_delete(g, id):
    """
    Api method for removing project
        :param g: context
        :param id: module id
    """
    g.id = id
    project_delete(g)
    return response_ok({
        'message':  'Project was removed.'
    })
