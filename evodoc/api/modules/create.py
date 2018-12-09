from evodoc.api.tools import response_ok_obj
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateData, ValidateToken
from evodoc.services.module import create
from flask import g


@modules.route('/module', methods=['POST'])
@ValidateToken()
@ValidateData(["project", "name", "description", "dependency", "content"])
def api_create():
    create()
    return response_ok_obj(g.module)
