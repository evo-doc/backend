from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate

class Module(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "module"
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.Text)
    active = sa.Column(sa.Boolean, default=True)
    project_id = sa.Column(sa.Integer, sa.ForeignKey("project.id"))
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    
    def __init__ (self, name=None, description=None, project_id=None, owner_id=None):
        self.name=name
        self.description=description
        self.project_id=project_id
        self.owner_id=owner_id