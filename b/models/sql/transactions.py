# library
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func

# others
from datetime import datetime

# files
from services.internal.sql.base import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[str] = mapped_column(nullable=False)
    is_deleted: Mapped[int] = mapped_column(default=0)
    is_modified: Mapped[int] = mapped_column(default=0)
    created_by: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
