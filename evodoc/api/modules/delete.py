from evodoc.api.tools import response_ok
from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateToken
from evodoc.services.module import module_delete
from flask import g


@modules.route('/<int:id>', methods=['DELETE'])
@ValidateToken()
def api_delete(id):
    g.id = id
    module_delete()
    return response_ok({
        'message':  'Module was deleted.'
    })
