from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import CreateUpdate

class UserToken(app.db.Model, CreateUpdate):
    __tablename__ = "user_token"
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    token = sa.Column(sa.String, unique=Tru, nullable=False)
    
    def __init__ (self, user_id=None, token=None):
        self.user_id=user_id
        self.token=token