from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate

class Package(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "package"
    name = sa.Column(sa.String(50), unique=True, nullable=False)
    description = sa.Column(sa.Text)
    url = sa.Column(sa.String, unique=True, nullable=False)
    active = sa.Column(sa.Boolean, default=True)
    
    def __init__ (self, name=None, description=None, url=None):
        self.name=name
        self.description=description
        self.url=url