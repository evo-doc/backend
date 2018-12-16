from flask import g, request
from evodoc.models.user import User
from evodoc.exception import ApiException
from evodoc.api.tools import response_ok_obj, response_ok
from evodoc.api.users import users, user
from evodoc.services.decorators import ValidateToken, ValidateData
from evodoc.services.users import update_user, delete_current_user,\
    user_change_passwd, get_users, get_user_accessible


@users.route('', methods=['GET'])
@ValidateToken()
def get_all():
    return response_ok(get_users())


@users.route('/<string:username>/account', methods=['GET'])
@ValidateToken()
def get_account(username):
    user = User.query.getByName(username, False)
    if user is None:
        raise ApiException(
            400, 'User was not found in database.', ['username'])
    return response_ok_obj(user)


@user.route('/account', methods=['GET'])
@ValidateToken()
def get_my_account():
    return response_ok_obj(g.token.user)


@user.route('/account', methods=['PATCH'])
@ValidateToken()
def edit_own_account():
    data = request.get_json()
    return response_ok_obj(update_user(data))


@user.route('/account', methods=['DELETE'])
@ValidateToken()
def delete_own_account():
    return response_ok(delete_current_user())


@user.route('/account/password', methods=['PATCH'])
@ValidateToken()
@ValidateData(['old_password', 'new_password'])
def change_password():
    return response_ok(user_change_passwd())


@user.route('/projects', methods=['POST'])
@ValidateToken()
@ValidateData(['limit'])
def get_accessible_project():
    return response_ok(get_user_accessible())
