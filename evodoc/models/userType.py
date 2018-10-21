from evodoc import app
import sqlalchemy as sa

class UserType(app.db.Model):
    __tablename__ = "user_type"
    name = sa.Column(sa.String(50), unique=True)
    users = app.db.relationship('User', backref='user_type', lazy=True)