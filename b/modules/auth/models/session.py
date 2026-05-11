# ------------------------- libraries -------------------------
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, Enum, DateTime, Index

from datetime import datetime, timezone, timedelta

# ------------------------------ files ------------------------------
from shared.database import Base

from auth.config.auth import APP_CONFIG


class Session(Base):
    __tablename__ = 'session'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False, unique=True)
    token_hash: Mapped[str] = mapped_column(nullable=False)
    
    device_name: Mapped[str] = mapped_column(nullable=False)
    user_agent: Mapped[str] = mapped_column(nullable=False)
    ip_address: Mapped[str] = mapped_column(nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    expired_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc) + timedelta(days=APP_CONFIG['session']['session_expiry_days']))
    last_activity_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    __table_args__ = (
        Index('idx_user_id', 'user_id'),
        # Index('idx_token_hash', 'token_hash'),
    )
    
    @property
    def details():
        return APP_CONFIG['db']['table']['session']
    
    
    