from evodoc.models import User
from evodoc import app
from evodoc.exception.dbException import DbException


def register(username, email, password):
    passwdHash = password  # TBA
    invalid = []
    try:
        if User.query.getByName(username, False) is not None:
            invalid.append("username")

        if User.query.getByEmail(email, False) is not None:
            invalid.append("email")

            user = User(name=username, email=email,
                        password=passwdHash, role_id=1)
            app.db.session.add(user)
            app.db.session.commit()
    except DbException as error:
        print(str(error))
    return user

    if invalid != []:
        raise DbException(
            400,
            "Sign up data are invalid or non-unique.",
            invalid=invalid)

    user = User(name=username, email=email, password=passwdHash, role_id=1)
    app.db.session.add(user)
    app.db.session.commit()
    return user.createToken().token
