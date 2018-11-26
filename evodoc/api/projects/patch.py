from evodoc.api.tools import response_ok_obj
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateToken
from evodoc.services.project import patch
from flask import g, request


@projects.route('/<int:id>', methods=['PATCH'])
@ValidateToken()
def api_patch(id):
    g.id = id
    g.data = request.get_json()
    patch()
    return response_ok_obj(g.project)
