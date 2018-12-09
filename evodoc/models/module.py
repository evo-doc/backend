from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate
from evodoc.models.module_to_module import ModuleDependencies
from evodoc.conf import FILE_PATH


class Module(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "module"
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.Text)
    active = sa.Column(sa.Boolean, default=True)
    project_id = sa.Column(sa.Integer, sa.ForeignKey("project.id"))
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    dependencies = app.db.relationship('Module',
        secondary=ModuleDependencies,  # noqa E128
        primaryjoin="Module.id == module_to_module.c.used_in_module_id",  # noqa E128
        secondaryjoin="Module.id == module_to_module.c.dependency_id",  # noqa E128
        backref='depended',  # noqa E128
        )  # noqa E128
    sa.UniqueConstraint('name', 'project_id', name='unique_name_in_project')

    def __init__(self, name=None, description=None,
                 project_id=None, owner_id=None):
        self.name = name
        self.description = description
        self.project_id = project_id
        self.owner_id = owner_id

    def serialize(self):
        """
        Serialize object for json
            :param self:
        """
        dependency = []
        for each in self.dependencies:
            dependency.append(each.name)

        if dependency == []:
            dependency = 'independent'

        content = ''
        with open(FILE_PATH +
                  '/' +
                  str(self.project_id) +
                  '/' +
                  str(self.id) +
                  '.json', 'r') as f:
            content = f.read()
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner_id,
            'project_id': self.project_id,
            'active': self.active,
            'created': self.create,
            'updated': self.update,
            'dependency': dependency,
            'content': content,
        }
