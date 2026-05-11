
# libraries

from pydantic import BaseModel
from datetime import datetime



# --------------------------- session ---------------------------
class TypeAuthSessionIn(BaseModel):
    user_id: int
    token_hash: str | None
    
    device_name: str | None
    user_agent: str | None
    ip_address: str | None
    
    
class TypeAuthSessionOut(BaseModel):
    user_id: int
    token_hash: str
    
    device_name: str
    user_agent: str
    ip_address: str
    
    created_at: datetime
    expired_at: datetime
    last_activity_at: datetime
    
class TypeAuthSessionCrate(BaseModel):
    user_id: int
    
    device_name: str
    user_agent: str
    ip_address: str
    
    