from evodoc import app
import sqlalchemy as sa
from evodoc.models.role_to_permission import RoleToPermission

class Role(app.db.Model):
    __tablename__ = "role"
    name = sa.Column(sa.String(50), unique=True, nullable=False)
    description = sa.Column(sa.Text)
    users = app.db.relationship('User', backref='role', lazy=True)
    permissions = app.db.relationship('Permission', secondary=RoleToPermission, lazy='subquery',
        backref=app.db.backref('role', lazy=True))
    
    def __init__ (self, name=None, description=None):
        self.name=name
        self.description=description