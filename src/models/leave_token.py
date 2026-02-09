from sqlalchemy import Column, String, DateTime, Text, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from .base import Base

class LeaveToken(Base):
    __tablename__ = 'leave_tokens'
    
    token = Column(UUID(as_uuid=True), primary_key=True)
    leave_data = Column(JSONB, nullable=False)
    action = Column(String(20))
    review_reason = Column(Text)
    processed_at = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    
    __table_args__ = (
        Index('idx_leave_created', 'created_at'),
        Index('idx_leave_processed', 'processed_at'),
    )