
# libraries

from pydantic import BaseModel
from datetime import datetime
# --------------------------- register ---------------------------

class TypeAuthLoginIn(BaseModel):
    email: str | None
    country_code: int  | None
    phone: int | None
    username: str  | None
    
    password: str
    
