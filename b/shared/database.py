# package
from sqlalchemy import create_engine, Index
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# other
from contextlib import contextmanager


# files
from config.config import DATABASE_PATH



engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


# Initial setup at starting:
def setup_db():
    # Create table
    Base.metadata.create_all(engine)
    


    
    
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
        
    
    

    