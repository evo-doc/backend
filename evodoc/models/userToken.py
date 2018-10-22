from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import CreateUpdate
from datetime import datetime, timedelta
from uuid import uuid4


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
            'update': self.update
        }

    def deleteWithPrevious(self):
        previousToken = UserToken.query.filter_by(
            id=self.previous_token_id).first()
        if previousToken is not None:
            previousToken.deleteWithPrevious()
        app.db.session.delete(self)
        app.db.session.commit()

    def createSuccessor(self):
        successor = UserToken.query.filter_by(
            previous_token_id=self.id).first()
        if successor is not None:
            return successor

        token = str(uuid4())

        # Check if token is unique
        while (UserToken.query.filter_by(token=token).count() != 0):
            token = str(uuid4())

        t = UserToken(
            user_id=self.user_id,
            token=token,
            previous_token_id=self.id)
        app.db.session.add(t)
        app.db.session.commit()
        return t
