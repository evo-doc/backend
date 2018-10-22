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

    @staticmethod
    def create_app():
        """
        Application factory, just something that creates your new favorite API
        """

        app = Evodoc(__name__)

        app.config.from_object("evodoc.conf")

        app.bcrypt = Bcrypt(app)

        from evodoc.basemodel import IdModel, naming_convention, GetOrQuery

        app.db = SQLAlchemy(app, model_class=IdModel, query_class=GetOrQuery,
                            metadata=MetaData(
                                naming_convention=naming_convention
                            ))

        migrate = Migrate(app, app.db, render_as_batch=True)  # noqa: F841

        from evodoc.api import homeprint, auth
        app.register_blueprint(homeprint)
        app.register_blueprint(auth)

        return app


app = Evodoc.create_app()
from evodoc.api.home import homeprint
app.register_blueprint(homeprint)

import evodoc.models

__all__ = [
    'app'
]
