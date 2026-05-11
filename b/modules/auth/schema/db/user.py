
# libraries

from pydantic import BaseModel
from datetime import datetime



# --------------------------- user ---------------------------
class TypeAuthUserGetIn(BaseModel):
    email: str | None
    phone: str | None
    username: str | None
    
    password: str | None
    
    
    
class TypeAuthUserCreateIn(BaseModel):
    email: str
    country_code: int
    phone: int
    username: str
    
    password_hash: str
    
    status: str = 'ACTIVE'
    role: str = 'USER'
    
    email_verified: int
    phone_verified: int
    
    
    
class TypeAuthUserCreateOut(BaseModel):
    email: str
    phone: int
    username: str
    
    status: str
    role: str
    
    email_verified: int
    phone_verified: int
    
    created_at: datetime

    
    
class TypeAuthUserLoginOut(BaseModel):
    user: dict | None
    session: dict | None
    

class TypeAuthUserLoginIn(BaseModel):
    email: str | None
    country_code: int  | None
    phone: int | None
    username: str  | None
    
    password: str