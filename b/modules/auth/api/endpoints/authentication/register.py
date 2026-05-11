# ----------------------- libraries -----------------------
from fastapi import APIRouter, status


# ----------------------- files -----------------------

# types
from modules.auth.schema.db.user import TypeAuthUserCreateIn, TypeAuthUserCreateOut
from Lending.b.modules.auth.schema.db.session import TypeAuthSessionIn

# db
from shared.database import get_db_session
from modules.auth.db.user import register_user
from modules.auth.db.session import get_session


# app:

auth_register = APIRouter()


# add user:
@auth_register.post('/', status_code=status.HTTP_201_CREATED)
def register(user: TypeAuthUserCreateIn):
    with get_db_session() as db:
        # add new user:
        new_user = register_user(db=db, user=user)
        
        # get new session:
        session = get_session(db=db, user_session=TypeAuthSessionIn(
            user_id=new_user.id
        ))
        
        # get access token:
        # access_token = get_access_token()
        
        return TypeAuthUserCreateOut(
            user=new_user,
            session=session
        )