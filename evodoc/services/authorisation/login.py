from evodoc.models import User
from evodoc.exception import ApiException


def login(nameOrEmail, passwd):
    user = User.query.getByNameOrEmail(nameOrEmail)

    if user is None or user.password != passwd:  # TBA
        raise ApiException(400, "Sign in data are invalid.")

    return {"token": user.createToken().token, "username": user.name}
