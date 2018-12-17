from evodoc.api.tools import response_ok_obj
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateToken
from evodoc.services.module import view
# from flask import g
from evodoc.services.decorators import CreateContext


@modules.route('/<int:id>', methods=['GET'])
@CreateContext()
@ValidateToken()
def api_view(g,id):
    g.id = id
    view(g)
    return response_ok_obj(g.module)
