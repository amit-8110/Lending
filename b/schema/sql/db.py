from dataclasses import dataclass


'''
    Models Schema
'''

@dataclass
class InsertAccountT:
    name: str
    notes: str
    types: str
    certified_by: str | None
    created_by: str
    # created_at: str | None
    
    
@dataclass
class TransactionT:
    description: str
    date: str | None
    # is_deleted: int
    # is_modified: int
    created_by: str
    # created_at: str | None
    accounts: list[EntryLineT]
    
    
@dataclass
class EntryLineT:
    idx: int | None     # check if new account or not.
    account: str
    notes: str | None
    types: str | None
    certified_by: str | None
    created_by: str | None
    debit: float = 0
    credit: float = 0
    
    
@dataclass
class JournalEntryT:
    transaction_id: int
    account_id: int
    account_name: str
    debit: int
    credit: int
    created_by: str
    
    
@dataclass
class ModifiedT:
    account_id: int | None
    transaction_id: int | None
    entry_id: int | None
    modified_id: int
    modified_notes: str
    modified_by: str