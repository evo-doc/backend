from evodoc import Evodoc
from flask_migrate import upgrade
import os
from pytest import fixture


@fixture
def client():
    """
    Fixture creating test client for evodoc app, initialize
    database and register blueprints
    """
    app = Evodoc.create_app("evodoc.testconf")
    client = app.test_client()
    with app.app_context():
        import evodoc.models  # noqa F401
        app.db.drop_all()
        app.db.create_all()
        upgrade(os.path.dirname(__file__) + '/../migrations')
        app.registerBlueprints()

    yield client

    with app.app_context():
        app.db.drop_all()
    # os.unlink('/tmp/test_evodoc.db')
