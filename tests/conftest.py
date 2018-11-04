import evodoc
from pytest import fixture


@fixture
def client():
    """
    Fixture creating test client for evodoc app, initialize
    database and register blueprints
    """
    app = evodoc.Evodoc.create_app()
    client = app.test_client()
    with app.app_context():
        app.db.drop_all()
        app.db.create_all()
        app.registerBlueprints()

    yield client

    app.db.drop_all()
