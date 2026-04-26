
# packages
from fastapi import APIRouter


# files
from api.v1.endpoints.transaction import tr_route as transaction_route

# router
v1_router = APIRouter()


# routes to transactions
v1_router.include_router(transaction_route, prefix='/tr', tags=['Transactions'])