from evodoc import app
import sqlalchemy as sa

ModuleDependencies = app.db.Table(
    'module_to_module',
    sa.Column('used_in_module_id',  # noqa E128
            sa.Integer,  # noqa E128
            sa.ForeignKey('module.id'),  # noqa E128
            primary_key=True),  # noqa E128
    sa.Column('dependency_id',  # noqa E128
            sa.Integer,  # noqa E128
            sa.ForeignKey('module.id'),   # noqa E128
            primary_key=True),  # noqa E128
)
