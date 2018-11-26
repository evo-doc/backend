from evodoc.api.tools import response_ok
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.project import addContributor
from flask import g


@projects.route('/<int:id>/users', methods=['POST'])
@ValidateToken()
@ValidateData(['username'])
def api_addContributor(id):
    g.id = id
    addContributor()
    return response_ok({
        'message': 'User added.'
    })
