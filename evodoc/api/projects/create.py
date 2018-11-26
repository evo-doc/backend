from evodoc.api.tools import response_ok_obj
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.project import create


@projects.route('/project', methods=['POST'])
@ValidateToken()
@ValidateData(["name", "description", "collaborators"])
def api_create():
    return response_ok_obj(create())
