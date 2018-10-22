from evodoc.models import User

def login(passwd, nameOrEmail):
    user = User.getByNameOrEmail(nameOrEmail)
    #check passwd TBA
    
    return user.createToken()