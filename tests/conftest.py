import evodoc
from pytest import fixture

@fixture
def client():
    app = evodoc.Evodoc.create_app()
    app.db.drop_all()
    app.db.create_all()
    client = app.test_client()
    from evodoc.api import homeprint, auth
    with app.app_context():
        app.register_blueprint(homeprint)
        app.register_blueprint(auth)


    yield client

    app.db.drop_all()
