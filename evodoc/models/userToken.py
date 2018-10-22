from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import CreateUpdate

class UserToken(app.db.Model, CreateUpdate):
    __tablename__ = "user_token"
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    previous_token_id = sa.Column(sa.Integer)
    token = sa.Column(sa.String, unique=True, nullable=False)
    
    def __init__ (self, user_id=None, token=None, previous_token_id=None):
        self.user_id=user_id
        self.token=token
        self.previous_token_id=previous_token_id

    def serialize(self):
        """
        Serialize object for json
            :param self:
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'token': self.token,
            'created': self.create,
            'updated': self.update
        }
