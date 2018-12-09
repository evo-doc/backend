from evodoc.api.tools import response_ok
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateToken
from evodoc.services.project import delete
from flask import g


@projects.route('/<int:id>', methods=['DELETE'])
@ValidateToken()
def api_delete(id):
    g.id = id
    delete()
    return response_ok({
        'message':  'Project was removed.'
    })
