from evodoc.models import User
from evodoc import app
from evodoc.exception.dbException import DbException
import re
from flask import g


def register():
    invalid = []
    if (not re.match('^[A-z0-9\_\-]{8,}$', g.data["username"]) or  # noqa W605
            User.query.getByName(g.data["username"], False) is not None):
        invalid.append("username")
    if (not re.match('[^@]+@[^@]+\.[^@]+', g.data["email"]) or  # noqa W605
            User.query.getByEmail(g.data["email"], False) is not None):
        invalid.append("email")
    if not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,})', g.data["password"]):
        invalid.append('password')
    passwdHash = g.data["password"]  # TBA
    if invalid != []:
        raise DbException(400,
                          "Sign up data are invalid or non-unique.",
                          invalid=invalid)

    user = User(name=g.data["username"], email=g.data["email"], password=passwdHash, role_id=1)
    app.db.session.add(user)
    app.db.session.commit()
    return {"token": user.createToken().token, "username": user.name}
