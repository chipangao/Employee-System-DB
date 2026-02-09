from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.sql import func
from .base import Base

class ShiftType(Base):
    __tablename__ = 'shift_types'
    
    id = Column(Integer, primary_key=True)
    shift_name = Column(String(50), nullable=False)
    description = Column(Text)
    sort_order = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_by = Column(String(50))
    created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<ShiftType(id={self.id}, shift_name='{self.shift_name}')>"