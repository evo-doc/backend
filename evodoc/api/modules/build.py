from evodoc.api.modules import modules
from evodoc.services.decorators import ValidateToken
from evodoc.services.module import build
from flask import send_file
from evodoc.services.decorators import CreateContext


@modules.route('/build/<int:id>', methods=['GET'])
@CreateContext()
@ValidateToken()
def api_build(g, id):
    g.id = id
    build(g)
    return send_file(g.pdf,
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=g.module.name + '.pdf')
