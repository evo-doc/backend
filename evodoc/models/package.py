from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate

class Package(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "package"
    name = sa.Column(sa.String(50))
    description = sa.Column(sa.Text)
    url = sa.Column(sa.String)
    active = sa.Column(sa.Boolean)