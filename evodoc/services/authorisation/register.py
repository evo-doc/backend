from evodoc.models import User, Role
from evodoc import app
from parse import parse
from evodoc.exception.dbException import DbException

def register (username, email, password):
    passwdHash=password #TBA
    invalid=[]
    if User.query.getByName(username,False)!=None:
        invalid.append("username")
    
    if User.query.getByEmail(email,False)!=None:
        invalid.append("email")

<<<<<<< HEAD
        user=User(name=username, email=email,password=passwdHash,role_id=1)
        app.db.session.add(user)
        app.db.session.commit()
    except IntegrityError:
        # dupe_field = parse('duplicate key value violates unique constraint "{constraint}"\nDETAIL:  Key ({field})=({input}) already exists.\n', str(IntegrityError.orig))["field"]
        print(str(IntegrityError.orig))
    return user
=======
    if invalid!=[]:
        raise DbException(400,"Sign up data are invalid or non-unique.",invalid=invalid)

    user=User(name=username, email=email,password=passwdHash,role_id=1)
    app.db.session.add(user)
    app.db.session.commit()
    return user.createToken().token
>>>>>>> authentication working
