from evodoc.api.tools import response_ok_list, response_ok_obj
from evodoc.api.users import users
from evodoc.services.decorators import ValidateToken
from evodoc.models.user import User
from flask import g


@users.route('', methods=['GET'])
@ValidateToken()
def get_all():
    return response_ok_list(User.query.get_all())


@users.route('/<string:username>/account', methods=['GET'])
@ValidateToken()
def get_account(username):
    return response_ok_obj(User.query.getByName(username))


@users.route('/account', methods=['GET'])
@ValidateToken()
def get_my_account():
    return response_ok_obj(g.token.user)