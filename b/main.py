
# library
from fastapi import FastAPI


# others


# files
from services.internal.sql.database import setup_db, get_db_session
from services.internal.sql.crud import record_transaction, TransactionT, EntryLineT, get_accounts


from api.v1.router import v1_router

# setup_db()

# with get_db_session() as db:
    # r = record_transaction(
    #     db=db,
    #     T=TransactionT(
    #         date='1/1/2026',
    #         description='Investment of 800 sold for 1000',
    #         created_by='Amit',
    #         accounts=[
    #             EntryLineT(
    #                 idx=None,
    #                 account='Bank',
    #                 notes='General Bank Account',
    #                 types='asset',
    #                 created_by='Amit',
    #                 certified_by=None,
    #                 debit=1000,
    #             ),
    #             EntryLineT(
    #                 idx=None,
    #                 certified_by=None,
    #                 account='Investment',
    #                 debit=800,
    #                 notes='General Investment Account',
    #                 types='asset',
    #                 created_by='Amit'
    #             ),
    #             EntryLineT(
    #                 idx=None,
    #                 certified_by=None,
    #                 account='Profit on Investment',
    #                 debit=200,
    #                 notes='General Bank Account',
    #                 types='asset',
    #                 created_by='Amit'
    #             )
    #         ]
    #     )
    # )
    

    # g = get_accounts(db=db, ids=[2])
    # for e in g:
    #     print(e.name)
    
    
app = FastAPI()

@app.get('/')
def main():
    return {'url': '/ :rootfile'}

# add router:
app.include_router(v1_router, prefix='/api/v1') # add the router's files: v1_router;


'''
    only pc: uvicorn main:app --reload
    across LN: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
'''