from evodoc import app
from evodoc.models import User


class Seeds():
    @classmethod
    def test_seeds(cls):
        """
        Seeds database with seeds
            :param cls:
        """
        testusers = [
            User("testuser", "test@login.com", 'Test@1010'),
            User("testuser2", "test2@login.com", 'Test@1010'),
            User("testuser3", "test3@login.com", 'Test@1010'),
        ]
        for user in testusers:
            app.db.session.add(user)

        app.db.session.flush()
        app.db.session.commit()
