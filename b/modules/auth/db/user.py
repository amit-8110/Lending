# ----------------------- libraries -----------------------
from sqlalchemy.orm import Session


# ----------------------- files -----------------------


# types
from modules.auth.schema.db.user import TypeAuthUserGet
from modules.auth.schema.db.user import TypeAuthUserCreateIn, TypeAuthUserCreateOut

# models
from modules.auth.models.user import User

# utils: hash
from shared.utils.crypto import _check_hash

# app:

def _get_user(db: Session, user: TypeAuthUserGet, auth_check: bool=False):
    result_user = db.query(User).where(
        User.email == user.email if user.email else
        User.phone == user.phone if user.phone else
        User.username == user.username
    ).one_or_none()
    
    if user and auth_check:
        ''' if password to check '''
        
        matched_password = _check_hash(password=user.password, hashed=result_user.password_hash)
        
        if matched_password: # if password matched
            return {
                "user": result_user,
                "password_verified": True
            }
        
        else:
            return {
                "user": result_user,
                "password_verified": False
            }

    else:
        return {
            "user": result_user,
            "password_verified": None
        }


def register_user(db: Session, user: TypeAuthUserCreateIn):
    new_user = User(
        email=user.email,
        country_code=user.country_code,
        phone=user.phone,
        username=user.username,
        
        password_hash=user.password_hash,
        
        status=user.status,
        role=user.role,
        
        email_verified=user.email_verified,
        phone_verified=user.phone_verified
    )
    
    db.add(new_user)
    
    db.commit()
    db.refresh(new_user)
    
    return TypeAuthUserCreateOut.model_validate(new_user)


