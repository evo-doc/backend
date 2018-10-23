from evodoc.models import User
from evodoc.exception import ApiException

def login(nameOrEmail, passwd):
    user = User.query.getByNameOrEmail(nameOrEmail)
    if user.password!=passwd: #TBA
        raise ApiException(400,"Sign in data are invalid.")

    return user.createToken().token
