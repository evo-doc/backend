from evodoc.api.tools import response_ok_obj
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.module import create
# from flask import g
from evodoc.services.decorators import CreateContext


@modules.route('/module', methods=['POST'])
@CreateContext()
@ValidateToken()
@ValidateData(["project", "name", "description", "dependency", "content"])
def api_create(g):
    """
    docstring here
        :param g: context
    """
    create(g)
    return response_ok_obj(g.module)
