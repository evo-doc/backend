from evodoc.api.tools import response_ok_obj
from evodoc.api.projects import projects
from evodoc.services.project import view
from evodoc.services.decorators import ValidateToken
# from flask import g
from evodoc.services.decorators import CreateContext


@projects.route('/<int:id>', methods=['GET'])
@CreateContext()
@ValidateToken()
def api_view(g, id):
    g.id = id
    view(g)
    return response_ok_obj(g.project)
