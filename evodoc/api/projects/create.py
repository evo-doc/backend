from evodoc.api.tools import response_ok
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.project import create


@projects.route('/project', methods=['POST'])
@ValidateToken()
@ValidateData(["name", "description", "collaborators"])
def create_project():
    return response_ok({
        'id': create().id
    })
