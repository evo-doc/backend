from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData


class Evodoc(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = None
        self.bcrypt = None
        self.database_seeds = None

    @staticmethod
    def create_app(conf="evodoc.conf"):
        """
        Application factory, just something that creates your new favorite API
        """

        app = Evodoc(__name__)

        app.config.from_object(conf)

        app.bcrypt = Bcrypt(app)

        from evodoc.basemodel import IdModel, naming_convention, GetOrQuery

        app.db = SQLAlchemy(app, model_class=IdModel, query_class=GetOrQuery,
                            metadata=MetaData(
                                naming_convention=naming_convention
                            ))

        migrate = Migrate(app, app.db, render_as_batch=True)  # noqa: F841

        return app

    def registerBlueprints(self):
        from evodoc.api import homeprint, auth, projects
        self.register_blueprint(homeprint)
        self.register_blueprint(auth)
        self.register_blueprint(projects)

    def init_seeds(self):
        from evodoc.services.seeds import Seeds
        app.database_seeds = Seeds()

    def test_seeds(self):
        app.database_seeds.test_seeds()


app = Evodoc.create_app()
app.registerBlueprints()
app.init_seeds()

import evodoc.models  # noqa F402 F401

__all__ = [
    'app'
]
