# library
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func, Index, Enum

# others
from datetime import datetime

# files
from services.internal.sql.base import Base



class Accounts(Base):
    __tablename__ = 'accounts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    notes: Mapped[str] = mapped_column(default='')
    types: Mapped[str] = mapped_column(
        Enum(
            'asset', 'liability', 'equity', 'expenses', 'income', name="account_type_enum"
        )
    )
    certified_by: Mapped[str] = mapped_column(nullable=True)
    is_modified: Mapped[int] = mapped_column(default=0)
    created_by: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        Index('idx_accounts_name', 'name'), # get Accounts by name.
        Index('idx_types', 'types'), # get Accounts certified or not.
        Index('idx_accounts_certified_by', 'certified_by') # get Accounts certified or not.
    )
        
    
