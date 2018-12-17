from evodoc.api.tools import response_ok
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.project import rmContributor
# from flask import g
from evodoc.services.decorators import CreateContext


@projects.route('/<int:id>/users', methods=['DELETE'])
@CreateContext()
@ValidateToken()
@ValidateData(['username'])
def api_rmContributor(g, id):
    g.id = id
    rmContributor(g)
    return response_ok({
        'message':  'User was removed.'
    })
