from evodoc import Evodoc
from flask_migrate import upgrade
import os
from pytest import fixture


@fixture(scope="session")
def app():
    app = Evodoc.create_app("evodoc.testconf")

    with app.app_context():
        app.registerBlueprints()

    yield app


@fixture(scope="session")
def db(app):
    with app.app_context():
        upgrade(os.path.dirname(__file__) + '/../migrations')
        app.db.create_all()

    yield app.db

    with app.app_context():
        app.db.reflect()
        app.db.drop_all()
    os.unlink("/tmp/test_evodoc.db")


@fixture(scope="session")
def client(app, db):
    """
    Fixture creating test client for evodoc app, initialize
    database and register blueprints
    """
    client = app.test_client()

    yield client
