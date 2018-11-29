from evodoc.api.tools import response_ok_list
from evodoc.api.users import users
from evodoc.services.decorators import ValidateToken
from evodoc.models.user import User


@users.route('', methods=['GET'])
@ValidateToken()
def get_all():
    return response_ok_list(User.query.get_all())
