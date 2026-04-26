# library
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func

# other
from datetime import datetime

# files
from services.internal.sql.base import Base

class Modified(Base):
    __tablename__ = 'modified'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[int | None] = mapped_column(nullable=True)
    transaction_id: Mapped[int | None] = mapped_column(nullable=True)
    entry_id: Mapped[int | None] = mapped_column(nullable=True)
    modified_id: Mapped[int] = mapped_column(nullable=False) # new replaced id:
    modified_notes: Mapped[str] = mapped_column(nullable=False)
    modified_by: Mapped[str] = mapped_column(nullable=False)
    modified_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    