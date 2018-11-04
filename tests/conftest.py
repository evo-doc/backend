import evodoc
from pytest import fixture

@fixture
def client():
    app = evodoc.Evodoc.create_app("evodoc.testconf")
    app.registerBlueprints()
    app.db.drop_all()
    app.db.create_all()
    client = app.test_client()

    yield client

    app.db.drop_all()
