from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate

class Module(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "module"
    name = sa.Column(sa.String(50))
    description = sa.Column(sa.Text)
    active = sa.Column(sa.Boolean)
    project_id = sa.Column(sa.Integer, sa.ForeignKey("project.id"))
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))