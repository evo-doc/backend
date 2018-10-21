from evodoc import app
import sqlalchemy as sa

UserTypeToPermission = app.db.Table('usertype_to_permission',
    sa.Column('user_type_id', sa.Integer, sa.ForeignKey('usertype.id'), primary_key=True),
    sa.Column('permission_id', sa.Integer, sa.ForeignKey('permission.id'), primary_key=True)
)