from evodoc.models import User
from evodoc import app
from evodoc.exception.dbException import DbException
import re


def register(username, email, password):
    invalid = []
    if (not re.match('^[A-z0-9\_\-]{3,}$', username) or  # noqa W605
            User.query.getByName(username, False) is not None):
        invalid.append("username")
    if (not re.match('[^@]+@[^@]+\.[^@]+', email) or  # noqa W605
            User.query.getByEmail(email, False) is not None):
        invalid.append("email")
    if not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})', password):
        invalid.append('password')
    passwdHash = password  # TBA
    if invalid != []:
        raise DbException(400,
                          "Sign up data are invalid or non-unique.",
                          invalid=invalid)

    user = User(name=username, email=email, password=passwdHash, role_id=1)
    app.db.session.add(user)
    app.db.session.commit()
    return {"token": user.createToken().token, "username": user.name}
