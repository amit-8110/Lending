# package
from sqlalchemy import create_engine, Index
from sqlalchemy.orm import sessionmaker
from services.internal.sql.base import Base

# other
from contextlib import contextmanager


# files
from configs.config import APP_CONFIG, DATABASE_PATH
from models.sql.accounts import Accounts
from models.sql.journal_entry import JournalEntries



engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=True)
Session = sessionmaker(bind=engine)


# Initial setup at starting:
def setup_db():
    # Create table
    Base.metadata.create_all(engine)
    
    # Crate Index
    
    
    # __table_args__
    # (Accounts)
    # Index('idx_accounts_name', Accounts.name) # get Accounts by name.
    # Index('idx_accounts_certified_by', Accounts.certified_by) # get Accounts certified or not.
    
    # # (Transaction)
    
    
    # # (Journal entry)
    # Index('idx_transaction_id', JournalEntries.transaction_id) # get Journal entry by Transaction id
    # Index('idx_account_id', JournalEntries.account_id) # get Journal entry by account id
    # Index('idx_account_name', JournalEntries.account_name) # get Journal entry by account name
    
    

    
    
# Make each ops session

'''
    @contextmanager enables the with statement.
    That decorator transforms your generator function into a context manager. So with get_session() as db:
    
    it needs 'yield'; 
    
    @contextmanager
    def get_session():
        db = Session()
        # --- SETUP (before yield) ---
        try:
            yield db          # ← caller gets `db` here, runs their code
        # --- TEARDOWN (after yield) ---
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()
            
            
    ***** without contextmanager:
        
    class get_session:
        def __enter__(self):
            self.db = Session()
            return self.db
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type:
                self.db.rollback()
            self.db.close()
'''

@contextmanager
def get_db_session():
    db = Session()
    
    try:
        yield db
        
    except Exception:
        db.rollback()
        raise
    
    finally:
        db.close()
        
    
    

    