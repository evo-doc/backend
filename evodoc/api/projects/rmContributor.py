from evodoc.api.tools import response_ok
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.project import rmContributor
from flask import g


@projects.route('/<int:id>/users', methods=['DELETE'])
@ValidateToken()
@ValidateData(['username'])
def api_rmContributor(id):
    g.id = id
    rmContributor()
    return response_ok({
        'message':  'User was removed.'
    })
