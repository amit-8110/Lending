# ----------------------- libraries -----------------------
from sqlalchemy.orm import Session
from datetime import datetime, timezone, timedelta

# ----------------------- files -----------------------


# types
from Lending.b.modules.auth.schema.db.session import TypeAuthSessionIn, TypeAuthSessionOut, TypeAuthSessionCrate

# models
from modules.auth.models.session import Session as SessionModel

# config
from modules.auth.config.auth import APP_CONFIG

# app:




# add_session:
def _remove_session(db: Session, session: TypeAuthSessionOut):
    db.delete(session)
    db.commit()
    
    return True


def _create_session(db: Session, session: TypeAuthSessionCrate):
    
    new_ss = SessionModel(
        user_id=session.user_id,
        token_hash=0,
    
        device_name=session.device_name,
        user_agent=session.user_agent,
        ip_address=session.ip_address
    )
    
    db.add(new_ss)
    db.commit()
    db.refresh(new_ss)
    
    return new_ss






'''
when getting session:
1. check if already has -> return it.
2. check if expired or not -> remove old + create new.
3.

'''

def get_session(db: Session, user_session: TypeAuthSessionIn):
    '''
        check if present or not.
    '''
    ss = db.query(Session).where(
        Session.user_id == user_session.user_id
    ).one_or_none()
    
    if ss:
        ''' session exist '''
        
        if int(ss.expired_at.timestamp()) < (datetime.now(timezone.utc) + timedelta(days=APP_CONFIG['session']['session_expiry_day'])).timestamp():
            ''' not expired '''
            
            return ss
        
        else:
            ''' expired '''
            removed = _remove_session(db=db, session=ss)
            
            if removed:
                new_ss = _create_session(db=db, session=TypeAuthSessionCrate(
                    user_id=user_session.user_id,
                    device_name=user_session.device_name,
                    user_agent=user_session.user_agent,
                    ip_address=user_session.ip_address
                ))
                
                return new_ss
                
            else:
                return False
            
        
    else:
        ''' session doesn't exist '''
        new_ss = _create_session(db=db, session=TypeAuthSessionCrate(
                    user_id=user_session.user_id,
                    device_name=user_session.device_name,
                    user_agent=user_session.user_agent,
                    ip_address=user_session.ip_address
                ))
                
        return new_ss
    




