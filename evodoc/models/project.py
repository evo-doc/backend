from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate
from evodoc.models.project_to_user import ProjectToUser


class Project(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "project"
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.Text)
    active = sa.Column(sa.Boolean, default=True)
    modules = app.db.relationship(
        'Module', backref='master_project', lazy=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    contributors = app.db.relationship('User', secondary=ProjectToUser,
                                       lazy='subquery',
                                       backref=app.db.backref(
                                            'contributed_project',
                                            lazy=True))

    def __init__(self, name=None, description=None, owner_id=None):
        self.name = name
        self.description = description
        self.owner_id = owner_id

    def serialize(self):
        """
        Serialize object for json
            :param self:
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner_id,
            'project_id': self.project_id,
            'active': self.active,
            'created': self.create,
            'updated': self.update
        }
