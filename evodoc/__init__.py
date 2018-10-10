from flask import Flask

def create_app():
    """
    Application factory, just something that creates your new favorite API
    """

    app = Flask(__name__)

    app.config.from_object("evodoc.conf")

    #Assigning app to SqlAlchemy
    from evodoc.models import db
    db.init_app(app)

    from evodoc.api.home import homeprint
    app.register_blueprint(homeprint)

    return app