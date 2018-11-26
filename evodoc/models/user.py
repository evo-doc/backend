from evodoc import app
import hashlib
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate
from evodoc.models.project_to_user import ProjectToUser
from uuid import uuid4
from evodoc.models.userToken import UserToken


class User(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "user"
    name = sa.Column(sa.String(50), unique=True)
    email = sa.Column(sa.String(120), unique=True)
    password = sa.Column(sa.String(128), nullable=False)
    active = sa.Column(sa.Boolean, default=True)
    activated = sa.Column(sa.Boolean, default=True)
    role_id = sa.Column(sa.Integer, sa.ForeignKey("role.id"))
    tokens = app.db.relationship('UserToken', backref='user', lazy=True)
    my_projects = app.db.relationship(
        'Project', backref='colaborating_user', lazy=True)
    my_modules = app.db.relationship('Module', backref='user', lazy=True)
    my_packages = app.db.relationship('Package', backref='user', lazy=True)
    projects = app.db.relationship('Project', secondary=ProjectToUser,
                                   lazy='subquery',
                                   backref=app.db.backref('owning_user',
                                                          lazy=True))

    def __init__(self, name=None, email=None, password=None, role_id=None):
        self.name = name
        self.email = email
        self.password = password  # hashed TBA
        self.role_id = role_id

    def serialize(self):
        """
        Serialize object for json
            :param self:
        """
        emailHash = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
        return {
            'id': self.id,
            'name': self.name,
            'emailhash': emailHash,
            'role_id': self.role_id,
            'activated': self.activated,
            'active': self.active,
            'created': self.create,
            'updated': self.update
        }

    def createToken(self):
        token = str(uuid4())

        # Check if token is unique
        while (UserToken.query.filter_by(token=token).count() != 0):
            token = str(uuid4())

        newTokenCls = UserToken(user_id=self.id, token=token)

        app.db.session.add(newTokenCls)
        app.db.session.commit()

        return newTokenCls
