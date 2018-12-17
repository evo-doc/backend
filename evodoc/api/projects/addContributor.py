from evodoc.api.tools import response_ok
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.project import addContributor
# from flask import g
from evodoc.services.decorators import CreateContext

@projects.route('/<int:id>/users', methods=['POST'])
@CreateContext()
@ValidateToken()
@ValidateData(['username'])
def api_addContributor(g, id):
    g.id = id
    addContributor(g)
    return response_ok({
        'message': 'User added.'
    })
