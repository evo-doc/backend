from evodoc.api.tools import response_ok_list, response_ok_obj, response_ok
from evodoc.api.users import users
from evodoc.services.decorators import ValidateToken
from evodoc.services.users import update_user, delete_current_user
from evodoc.models.user import User
from flask import g, request


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


@users.route('/account', methods=['PATCH'])
@ValidateToken()
def edit_own_account():
    data = request.get_json()
    return response_ok_obj(update_user(data))

@users.route('/account', methods=['DELETE'])
@ValidateToken()
def delete_own_account():
    return response_ok(delete_current_user())

