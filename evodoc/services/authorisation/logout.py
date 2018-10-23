from evodoc.models import UserToken

def logout(token):
    t = UserToken.query.filter_by(token=token).first()
    if t!=None:
        t.deleteWithPrevious()
