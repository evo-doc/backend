from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate

class Package(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "package"
    name = sa.Column(sa.String(50), unique=True, nullable=False)
    description = sa.Column(sa.Text)
    url = sa.Column(sa.String, unique=True, nullable=False)
    active = sa.Column(sa.Boolean, default=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    
    def __init__ (self, name=None, description=None, url=None, owner_id=None):
        self.name=name
        self.description=description
        self.url=url
        self.owner_id=owner_id

    def serialize(self):
        """
        Serialize object for json
            :param self:
        """
        return {
            'id': self.id,
            'name': self.name,
            'description':self.description,
            'url': self.url,
            'active': self.active,
            'created': self.create,
            'updated': self.update,
            'owner_id': self.owner_id
        }