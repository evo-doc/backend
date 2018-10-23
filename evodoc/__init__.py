from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

class Evodoc(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = None

    @staticmethod
    def create_app():
        """
        Application factory, just something that creates your new favorite API
        """

        app = Evodoc(__name__)

        app.config.from_object("evodoc.conf")

        from evodoc.basemodel import IdModel, naming_convention, GetOrQuery
        app.db = SQLAlchemy(app, model_class=IdModel, query_class=GetOrQuery, metadata=MetaData(naming_convention=naming_convention))


        migrate = Migrate(app, app.db, render_as_batch=True)

        return app

app = Evodoc.create_app()

from evodoc.api import homeprint, auth
app.register_blueprint(homeprint)
app.register_blueprint(auth)

import evodoc.models

__all__ = [
    'app'
]