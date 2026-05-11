# ----------------------- libraries -----------------------
from fastapi import APIRouter, status


# ----------------------- files -----------------------

# types
from modules.auth.schema.api.login import TypeAuthLoginIn
from modules.auth.schema.api.authentication import TypeAuthRegisterLoginOut
from modules.auth.schema.api.session import TypeAuthSessionIn
from modules.auth.schema.db.user import TypeAuthUserGet

# db
from shared.database import get_db_session
from modules.auth.db.session import get_session
from modules.auth.db.user import _get_user

# app:

login_register = APIRouter()


# add user:
@login_register.post('/', status_code=status.HTTP_201_CREATED) # /login/
def login(user: TypeAuthLoginIn):
    with get_db_session() as db:
        
        # find user:
        find_user = _get_user(db=db, user=TypeAuthUserGet(
            email=user.email,
            phone=user.phone,
            username=user.username,
            password=user.password
        ), auth_check=True)
        
        if find_user:
            '''if user found '''
            if find_user['password_verified']:
                # get new session:
                session = get_session(db=db, user_session=TypeAuthSessionIn(
                    user_id=find_user['user'].id
                ))
                
                return TypeAuthRegisterLoginOut(
                    user=find_user['user'],
                    session=session
                )
            
            else:
                return TypeAuthRegisterLoginOut(
                    user=find_user['user'],
                    session=None
                )
            
        else:
            return TypeAuthRegisterLoginOut(
                    user=None,
                    session=None
                )
            
        
        
        
        # get access token:
        # access_token = get_access_token()
        
        return {
                "user": new_user,
                "session": session
        }