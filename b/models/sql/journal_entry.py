# library
from sqlalchemy import ForeignKey, DateTime, func, Index
from sqlalchemy.orm import Mapped, mapped_column


# others
from datetime import datetime

# files
from services.internal.sql.base import Base


class JournalEntries(Base):
    __tablename__ = 'journal_entries'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    transaction_id: Mapped[int] = mapped_column(ForeignKey('transactions.id'), nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey('accounts.id'), nullable=False)
    account_name: Mapped[str] = mapped_column(nullable=False)
    created_by: Mapped[str] = mapped_column(nullable=False)
    debit: Mapped[int] = mapped_column(default=0)
    credit: Mapped[int] = mapped_column(default=0)
    is_deleted: Mapped[int] = mapped_column(default=0)
    is_modified: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    
    __table_args__ = (
        Index('idx_transaction_id', 'transaction_id'), # get Journal entry by Transaction id
        Index('idx_account_id', 'account_id'), # get Journal entry by account id
        Index('idx_account_name', 'account_name') # get Journal entry by account name
    )
    
    

    
