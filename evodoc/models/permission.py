from evodoc import app
import sqlalchemy as sa

class Permission(app.db.Model):
    __tablename__ = "permission"
    name = sa.Column(sa.String(20), unique=True)
    description = sa.Column(sa.String)