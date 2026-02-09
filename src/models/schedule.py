from sqlalchemy import Column, Integer, ForeignKey, Date, String, DateTime, Text, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Schedule(Base):
    __tablename__ = 'schedules'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    schedule_date = Column(Date, nullable=False)
    week_number = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    shift_name = Column(String(50))
    shift_description = Column(Text)
    user_name_snapshot = Column(String(100))
    created_by = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    remark = Column(Text)
    
    user = relationship("User", backref="schedules")
    
    __table_args__ = (
        Index('idx_schedules_date', 'schedule_date'),
        Index('idx_schedules_user_date', 'user_id', 'schedule_date'),
        Index('idx_schedules_user_snapshot', 'user_name_snapshot'),
        Index('idx_schedules_week_year', 'week_number', 'year'),
    )