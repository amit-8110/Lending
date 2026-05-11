
# ----------------------- library -----------------------

from fastapi import APIRouter


# ----------------------- files -----------------------

from auth.api.endpoints.authentication.register import auth_register
from auth.api.endpoints.authentication.login import login_register



auth_router = APIRouter()


auth_router.include_router(auth_register, prefix='/register')
auth_router.include_router(login_register, prefix='/login')



@auth_router.get('/') # api/auth/
def f(ids: str):
    return 'api/auth/: home'