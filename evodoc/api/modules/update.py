from evodoc.api.tools import response_ok_obj
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateToken
from evodoc.services.module import update
from flask import g, request


@modules.route('/<int:id>', methods=['PATCH'])
@ValidateToken()
def api_update(id):
    g.id = id
    g.data = request.get_json()
    update()
    return response_ok_obj(g.module)
