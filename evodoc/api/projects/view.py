from evodoc.api.tools import response_ok_obj
from evodoc.api.projects import projects
from evodoc.services.project import view
from flask import g


@projects.route('/<int:id>', methods=['GET'])
def api_view(id):
    g.id = id

    return response_ok_obj(view())
