from evodoc.api.tools import response_ok_obj
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateToken
from evodoc.services.module import update
from flask import request
from evodoc.services.decorators import CreateContext


@modules.route('/<int:id>', methods=['PATCH'])
@CreateContext()
@ValidateToken()
def api_update(g, id):
    """
    Api method for updating module
        :param g: context
        :param id: module id
    """
    g.id = id
    g.data = request.get_json()
    update(g)
    return response_ok_obj(g.module)
