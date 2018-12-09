from evodoc.api.tools import response_ok_obj
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateToken
from evodoc.services.module import view
from flask import g


@modules.route('/<int:id>', methods=['GET'])
@ValidateToken()
def api_view(id):
    g.id = id
    view()
    return response_ok_obj(g.module)
