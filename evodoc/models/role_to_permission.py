from evodoc import app
import sqlalchemy as sa

RoleToPermission = app.db.Table('role_to_permission',
    sa.Column('role_id', sa.Integer, sa.ForeignKey('role.id'), primary_key=True),
    sa.Column('permission_id', sa.Integer, sa.ForeignKey('permission.id'), primary_key=True)
)