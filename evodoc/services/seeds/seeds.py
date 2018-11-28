from evodoc import app
from evodoc.models import User


class Seeds():
    @classmethod
    def test_seeds(cls):
        testusers = [
            User("testuser", "test@login.com", 'Test@1010')
        ]
        for user in testusers:
            app.db.session.add(user)

        app.db.session.flush()
        app.db.session.commit()