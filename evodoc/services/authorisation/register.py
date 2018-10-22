from evodoc.models import User, Role
from evodoc import app
from sqlalchemy.exc import IntegrityError
from parse import parse

def register (username, email, password):
    passwdHash=password #TBA
    try:
    # role=Role("kek")
    # app.db.session.add(role)
    # app.db.session.commit()

        user=User(name=username, email=email,password=passwdHash,role_id=1)
        app.db.session.add(user)
        app.db.session.commit()
    except IntegrityError:
        # dupe_field = parse('duplicate key value violates unique constraint "{constraint}"\nDETAIL:  Key ({field})=({input}) already exists.\n', str(IntegrityError.orig))["field"]
        print(str(IntegrityError.orig))
    return user