from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate
from evodoc.models.project_to_user import ProjectToUser
import hashlib
from evodoc.models.user import User
from evodoc.exception import DbException


class Project(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "project"
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.Text)
    active = sa.Column(sa.Boolean, default=True)
    modules = app.db.relationship(
        'Module', primaryjoin='and_(Module.project_id==Project.id, '
                              'Module.delete.is_(None))')
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
        contrib = []
        for each in self.contributors:
            contrib.append([
                each.name,
                hashlib.md5(each.email.lower().encode('utf-8')).hexdigest(),
                'contributor',
            ])

        colab = {
            'label': [
                "username",
                "emailhash",
                "role",
            ],
            'data': contrib,
        }
        owner = User.query.get_or(self.owner_id)
        if owner is None:
            raise DbException(404, "Owner not found.", ['owner_id'])
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner': {
                'id': self.owner_id,
                'username': owner.name,
                'emailhash': hashlib.md5(
                    owner.email.lower().encode('utf-8')
                ).hexdigest(),
            },
            'collaborators': colab,
            'active': self.active,
            'created': self.create,
            'updated': self.update
        }
