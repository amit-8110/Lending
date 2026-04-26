
# library
from fastapi import APIRouter


# files
from services.internal.sql.database import get_db_session
from services.internal.sql.crud import get_accounts

tr_route = APIRouter()

@tr_route.get('/{ids}')
def tr(ids: str):
    with get_db_session() as db:
        g = get_accounts(db=db, ids=ids.split(',') if ',' in ids else ids)
        return g
