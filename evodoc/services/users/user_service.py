from evodoc.models import User, Project
from evodoc.exception import DbException, ApiException
from flask import g
import re
import datetime
from evodoc import app


class UsersListDTO():
    label = [
        'username',
        'email',
    ]
    data = []

    def add_user(self, user_data):
        self.data.append(user_data)

    def seriliaze(self):
        return {
            'label': self.label,
            'data': self.data,
        }


class ProjectListDTO():
    label = [
        "id",
        "owner",
        "name",
        "description",
        "version"
    ]
    data = []
    limit = 0

    def __init__(self, limit=0):
        self.limit = limit

    def add_project(self, project_data):
        if len(self.data) <= self.limit:
            self.data.append(project_data)

    def seriliaze(self):
        return {
            'label': self.label,
            'data': self.data,
        }


def get_users():
    users = User.query.filter(User.id != g.token.user.id)
    result = UsersListDTO()
    for user in users:
        data = [
            user.name,
            user.email,
        ]
        result.add_user(data)

    return {'users': result.seriliaze()}


def update_user(data):
    user_up = g.token.user
    if ('username' in data
            and data['username'] is not None):
        user = User.query.getByName(data['username'], False)
        if user is not None:
            raise DbException(400,
                              "This username is already in use.",
                              ['username'])
        else:
            user_up.name = data['username']

    if ('email' in data
            and data['email'] is not None):
        if not re.match('[^@]+@[^@]+\.[^@]+', data["email"]):  # noqa W605
            raise ApiException(400, "Supplied email is not valid.", ['email'])
        user = User.query.getByEmail(data['email'], False)
        if user is not None:
            raise DbException(400,
                              "This email is already in use.",
                              ['email'])
        else:
            user_up.email = data['email']

    if ('name' in data and data['name'] is not None):
        user_up.fullname = data['name']

    app.db.session.flush()
    app.db.session.commit()

    return user_up


def delete_current_user():
    user_up = g.token.user

    user_up.delete = datetime.datetime.utcnow()
    user_up.active = False

    app.db.session.flush()
    app.db.session.commit()

    return {
        'message': 'User account was deleted.'
    }


def user_change_passwd():
    user_up = g.token.user

    if not app.bcrypt.check_password_hash(user_up.password,
                                          g.data['old_password']):
        raise ApiException(400, 'Invalid old password.', ['old_password'])

    if not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})',
                    g.data['new_password']):
        raise ApiException(400, 'Invalid new password.', ['new_password'])

    user_up.password = app.bcrypt.generate_password_hash(
        g.data['new_password'])

    app.db.session.flush()
    app.db.session.commit()

    return {
        'message': 'User password was changed.'
    }


def get_user_accessible():
    try:
        limit = int(g.data['limit'])
    except ValueError:
        raise ApiException(400, 'Invalid limit.', ['limit'])

    if limit < 0:
        raise ApiException(400, 'Invalid limit.', ['limit'])
    user_up = g.token.user
    result = ProjectListDTO(limit)
    owned_project = Project.query.filter(Project.owner_id == user_up.id)

    for project in owned_project:
        data = [
            project.id,
            user_up.name,
            "",
            "",
            ""
        ]
        result.add_project(data)

    connected = Project.query.filter(Project.contributors.contains(user_up))

    for connection in connected:
        project = Project.query.filter(Project.id == connection.project_id)
        data = [
            project.id,
            user_up.name,
            "",
            "",
            ""
        ]
        result.add_project(data)

    return {'projects': result.seriliaze()}
