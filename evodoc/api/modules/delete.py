from evodoc.api.tools import response_ok
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateToken
from evodoc.services.module import module_delete
# from flask import g
from evodoc.services.decorators import CreateContext


@modules.route('/<int:id>', methods=['DELETE'])
@CreateContext()
@ValidateToken()
def api_delete(g, id):
    """
    Api method for module deletion
        :param g: context
        :param id: module id
    """
    g.id = id
    module_delete(g)
    return response_ok({
        'message':  'Module was deleted.'
    })
