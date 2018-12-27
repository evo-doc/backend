from evodoc.api.tools import response_ok_obj
from evodoc.api.projects import projects
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.project import create
# from flask import g
from evodoc.services.decorators import CreateContext


@projects.route('/project', methods=['POST'])
@CreateContext()
@ValidateToken()
@ValidateData(["name", "description", "collaborators"])
def api_create(g):
    """
    Api method for creating new project
        :param g: context
    """
    create(g)
    return response_ok_obj(g.project)
