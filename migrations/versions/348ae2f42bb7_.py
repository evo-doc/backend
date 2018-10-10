"""empty message

Revision ID: 348ae2f42bb7
Revises: 
Create Date: 2018-10-10 12:25:44.391467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '348ae2f42bb7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_type',
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_type')),
    sa.UniqueConstraint('name', name=op.f('uq_user_type_name'))
    )
    op.create_table('user',
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('update', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('activated', sa.Boolean(), nullable=True),
    sa.Column('user_type_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_type_id'], ['user_type.id'], name=op.f('fk_user_user_type_id_user_type')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('name', name=op.f('uq_user_name'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('user_type')
    # ### end Alembic commands ###
