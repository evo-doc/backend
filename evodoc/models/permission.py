from evodoc import app
import sqlalchemy as sa
from evodoc.models.role_to_permission import RoleToPermission

class Permission(app.db.Model):
    __tablename__ = "permission"
    name = sa.Column(sa.String(20), unique=True)
    description = sa.Column(sa.String)
    roles = app.db.relationship('Role', secondary=RoleToPermission, lazy='subquery',
        backref=app.db.backref('permission', lazy=True))