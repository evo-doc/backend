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
<<<<<<< HEAD
        user=User(name=username, email=email,password=passwdHash,role_id=1)
        app.db.session.add(user)
        app.db.session.commit()
    except IntegrityError:
        # dupe_field = parse('duplicate key value violates unique constraint "{constraint}"\nDETAIL:  Key ({field})=({input}) already exists.\n', str(IntegrityError.orig))["field"]
        print(str(IntegrityError.orig))
    return user
=======
=======
>>>>>>> 3a87d36124975b2e832402d1629f26741887965d
    if invalid!=[]:
        raise DbException(400,"Sign up data are invalid or non-unique.",invalid=invalid)

    user=User(name=username, email=email,password=passwdHash,role_id=1)
    app.db.session.add(user)
    app.db.session.commit()
<<<<<<< HEAD
    return user.createToken().token
>>>>>>> authentication working
=======
    return user.createToken().token
>>>>>>> 3a87d36124975b2e832402d1629f26741887965d
