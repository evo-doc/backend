from evodoc import app
import sqlalchemy as sa

ProjectToUser = app.db.Table('project_to_user',
                             sa.Column(
                                 'project_id',
                                 sa.Integer,
                                 sa.ForeignKey('project.id'),
                                 primary_key=True),
                             sa.Column(
                                 'user_id',
                                 sa.Integer,
                                 sa.ForeignKey('user.id'),
                                 primary_key=True)
                             )
