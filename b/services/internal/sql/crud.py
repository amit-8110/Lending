
# package
from sqlalchemy import select
from sqlalchemy.orm import Session


# other

# files
from models.sql.accounts import Accounts
from models.sql.transactions import Transaction
from models.sql.journal_entry import JournalEntries


from schema.sql.db import InsertAccountT, TransactionT, EntryLineT, JournalEntryT


# INSERT
def record_account(db: Session, acc: InsertAccountT):
    new_acc = Accounts(
        name=acc.name,
        notes=acc.notes,
        types=acc.types,
        certified_by=acc.certified_by,
        created_by=acc.created_by
    )
    
    
    db.add(new_acc)
    db.commit()
    db.refresh(new_acc)
    
    return new_acc


def record_journal_entry(db: Session, J: JournalEntryT):
    new_ent = JournalEntries(
        transaction_id=J.transaction_id,
        account_id=J.account_id,
        account_name=J.account_name,
        debit=J.debit,
        credit=J.credit,
        created_by=J.created_by
    )
    
    
    db.add(new_ent)
    db.commit()
    db.refresh(new_ent)
    
    return new_ent


def record_transaction(db: Session, T: TransactionT):
    entry_=[]
    
    
    new_tr = Transaction(
        date=T.date,
        description=T.description,
        created_by=T.created_by
    )
    
    
    db.add(new_tr)
    db.commit()
    db.refresh(new_tr)
    
    # add entry
    for entry in T.accounts:
        if entry.idx == None:
            '''
            This Invoke, when a accounts is new (Non-certified), but get registered.
            '''
            added_acc = record_account(db=db, acc=InsertAccountT(
                name=entry.account,
                notes=entry.notes,
                types=entry.types,
                certified_by=entry.certified_by,
                created_by=entry.created_by,
            ))
            
            added_entry = record_journal_entry(db=db, J=JournalEntryT(
                    transaction_id=new_tr.id,
                    account_id=added_acc.id,
                    account_name=entry.account,
                    debit=entry.debit,
                    credit=entry.credit,
                    created_by=entry.created_by
                )
            )
            
            # Update entry id
            entry_.append(added_entry)
            
        else:
            '''
            This invoke, when accounts is not new, may be or may not be certified.
            '''
            
            added_entry = record_journal_entry(db=db, J=JournalEntryT(
                    transaction_id=new_tr.id,
                    account_id=entry.idx,
                    account_name=entry.account,
                    debit=entry.debit,
                    credit=entry.credit,
                    created_by=entry.created_by
                )
            )
            # Update entry id
            entry_.append(added_entry)
            
    return {
        "status": True,
        "transaction_id": new_tr,
        "added_entries": entry_
    }
    
    

# READ


def get_accounts(db: Session, ids: list):
    q = select(Accounts).where(Accounts.id.in_(ids if isinstance(ids, list) else [ids]))
    r = db.execute(q)
    
    return r.scalars().all()




















'''
search by timezone

    ```python
        from datetime import datetime, timezone
        from sqlalchemy import select

        start = datetime(2026, 4, 1, tzinfo=timezone.utc)
        end = datetime(2026, 5, 1, tzinfo=timezone.utc)

        stmt = select(Transaction).where(
            Transaction.created_at >= start,
            Transaction.created_at < end
        )

        rows = session.execute(stmt).scalars().all()

    ```


    Best practice:

    start≤created_at<end

    Use < end instead of <= end to avoid edge-case bugs.



'''
