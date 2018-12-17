from evodoc.api.tools import response_ok_obj
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateToken
from evodoc.services.project import patch
from flask import request
from evodoc.services.decorators import CreateContext


@projects.route('/<int:id>', methods=['PATCH'])
@CreateContext()
@ValidateToken()
def api_patch(g, id):
    g.id = id
    g.data = request.get_json()
    patch(g)
    return response_ok_obj(g.project)
