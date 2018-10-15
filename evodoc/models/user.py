import datetime
from evodoc import app
import sqlalchemy as sa

class User(app.db.Model):
    __tablename__ = "user"
    name = sa.Column(sa.String(50), unique=True)
    email = sa.Column(sa.String(120), unique=True)
    password = sa.Column(sa.String(128), nullable=False)
    created = sa.Column(sa.DateTime, default=datetime.datetime.utcnow())
    update = sa.Column(sa.DateTime, default=datetime.datetime.utcnow())
    active = sa.Column(sa.Boolean)
    activated = sa.Column(sa.Boolean)
    user_type_id = sa.Column(sa.Integer, sa.ForeignKey("user_type.id"))

class UserType(app.db.Model):
    __tablename__ = "user_type"
    name = sa.Column(sa.String(50), unique=True)
    users = app.db.relationship('User', backref='user_type', lazy=True)