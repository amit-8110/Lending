# ------------------------- libraries -------------------------
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, Enum, DateTime, Index

from datetime import datetime, timezone

# ------------------------------ files ------------------------------
from shared.database import Base

from auth.config.auth import APP_CONFIG


class User(Base):
    __tablename__ = 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    country_code: Mapped[int] = mapped_column(nullable=False)
    phone: Mapped[int] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    
    password_hash: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(Enum(
        APP_CONFIG['db']['table']['user']['enum']['status']
    ), default='ACTIVE')
    
    role: Mapped[str] = mapped_column(Enum(
        APP_CONFIG['db']['table']['user']['enum']['role']
    ), default='USER')
    
    email_verified: Mapped[int] = mapped_column(default=0)
    phone_verified: Mapped[int] = mapped_column(default=0)
    
    last_login_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    
    is_deleted: Mapped[int] = mapped_column(default=0)
    
    
    
    __table_args__ = (
        Index('idx_email', 'email'),
        Index('idx_phone', 'phone'),
        Index('idx_username', 'username')
    )
    
    @property
    def details():
        return APP_CONFIG['db']['table']['user']
    
    
    