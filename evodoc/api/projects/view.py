from evodoc.api.tools import response_ok_obj
from evodoc.api.projects import projects
from evodoc.services.project import view
from evodoc.services.decorators import ValidateToken
from flask import g


@projects.route('/<int:id>', methods=['GET'])
@ValidateToken()
def api_view(id):
    g.id = id
    view()
    return response_ok_obj(g.project)
