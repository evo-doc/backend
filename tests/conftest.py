import evodoc
from pytest import fixture


@fixture
def client():
    app = evodoc.Evodoc.create_app()
    client = app.test_client()
    from evodoc.api import homeprint, auth
    with app.app_context():
        app.db.drop_all()
        app.db.create_all()
        app.register_blueprint(homeprint)
        app.register_blueprint(auth)

    yield client

    app.db.drop_all()
