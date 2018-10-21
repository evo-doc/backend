import datetime
from evodoc import app
import sqlalchemy as sa
from evodoc.basemodel import SoftDelete, CreateUpdate

class User(app.db.Model, SoftDelete, CreateUpdate):
    __tablename__ = "user"
    name = sa.Column(sa.String(50), unique=True)
    email = sa.Column(sa.String(120), unique=True)
    password = sa.Column(sa.String(128), nullable=False)
    active = sa.Column(sa.Boolean)
    activated = sa.Column(sa.Boolean)
    user_type_id = sa.Column(sa.Integer, sa.ForeignKey("user_type.id"))
    tokens = app.db.relationship('UserToken', backref='user', lazy=True)