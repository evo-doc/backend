from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate
from evodoc.models.project_to_user import ProjectToUser

class User(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "user"
    name = sa.Column(sa.String(50), unique=True)
    email = sa.Column(sa.String(120), unique=True)
    password = sa.Column(sa.String(128), nullable=False)
    active = sa.Column(sa.Boolean, default=True)
    activated = sa.Column(sa.Boolean, default=False)
    role_id = sa.Column(sa.Integer, sa.ForeignKey("role.id"))
    tokens = app.db.relationship('UserToken', backref='user', lazy=True)
    my_projects = app.db.relationship('Project', backref='user', lazy=True)
    my_modules = app.db.relationship('Module', backref='user', lazy=True)
    projects = app.db.relationship('Project', secondary=ProjectToUser, lazy='subquery',
        backref=app.db.backref('user', lazy=True))
    
    def __init__ (self, name=None, email=None, password=None, role_id=None):
        self.name=name
        self.email=email
        self.password=password # hashed TBA
        self.role_id=role_id