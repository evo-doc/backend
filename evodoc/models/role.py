from evodoc import app
import sqlalchemy as sa

class Role(app.db.Model):
    __tablename__ = "role"
    name = sa.Column(sa.String(50), unique=True)
    users = app.db.relationship('User', backref='role', lazy=True)