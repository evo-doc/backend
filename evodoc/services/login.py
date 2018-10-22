from evodoc.models import user

def login(passwd, nameOrEmail):
    user=User.getByNameOrEmail(nameOrEmail)
    #check passwd TBA

    #create&return token TBA