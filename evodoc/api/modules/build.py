from evodoc.api.modules import modules
from evodoc.services.module import build
from flask import send_file, request
from evodoc.services.decorators import CreateContext
from evodoc.models import UserToken
from datetime import datetime
from evodoc.exception import ApiException


@modules.route('/build/<int:id>', methods=['GET'])
@CreateContext()
def api_build(g, id):
    """
    Api method for module build
        :param g: Context bearing token
        :param id: Module ID
        :param token: User token
    """
    token = request.args.get('token', default='0', type=str)

    tokenObject = UserToken.query.filter_by(token=token).first()

    if tokenObject is None:
        raise ApiException(
            401,
            "Unauthorised user (missing or outdated token)",
            ['token'])

    if tokenObject.update <= datetime.utcnow():
        tokenObject = tokenObject.createSuccessor()

    g.token = tokenObject
    g.id = id

    build(g)

    return send_file(g.pdf,
                     mimetype='application/pdf',
                     as_attachment=True,
                     attachment_filename=g.module.name + '.pdf')
