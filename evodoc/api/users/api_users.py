from flask import request
from evodoc.models.user import User
from evodoc.exception import ApiException
from evodoc.api.tools import response_ok_obj, response_ok
from evodoc.api.users import users, user
from evodoc.services.decorators import ValidateToken, ValidateData
from evodoc.services.users import update_user, delete_current_user,\
    user_change_passwd, get_users, get_user_accessible
from evodoc.services.decorators import CreateContext


@users.route('', methods=['GET'])
@CreateContext()
@ValidateToken()
def get_all(g):
    return response_ok(get_users(g))


@users.route('/<string:username>/account', methods=['GET'])
@CreateContext()
@ValidateToken()
def get_account(g,username):
    user = User.query.getByName(username, False)
    if user is None:
        raise ApiException(
            400, 'User was not found in database.', ['username'])
    return response_ok_obj(user)


@user.route('/account', methods=['GET'])
@CreateContext()
@ValidateToken()
def get_my_account(g):
    return response_ok_obj(g.token.user)


@user.route('/account', methods=['PATCH'])
@CreateContext()
@ValidateToken()
def edit_own_account(g):
    data = request.get_json()
    return response_ok_obj(update_user(g,data))


@user.route('/account', methods=['DELETE'])
@CreateContext()
@ValidateToken()
def delete_own_account(g):
    return response_ok(delete_current_user(g))


@user.route('/account/password', methods=['PATCH'])
@CreateContext()
@ValidateToken()
@ValidateData(['old_password', 'new_password'])
def change_password(g):
    return response_ok(user_change_passwd(g))


@user.route('/projects', methods=['POST'])
@CreateContext()
@ValidateToken()
@ValidateData(['limit'])
def get_accessible_project(g):
    return response_ok(get_user_accessible(g))
