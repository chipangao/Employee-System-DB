from sqlalchemy import Column, Integer, String, DateTime, Date, CheckConstraint
from sqlalchemy.sql import func
from .base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    userid = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password_hash = Column(String(255), nullable=False)
    nickname = Column(String(100))
    email = Column(String(255))
    role_level = Column(Integer, default=2)
    status = Column(Integer, default=1)
    last_login = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    phone = Column(String(20))
    department_id = Column(Integer)
    hire_date = Column(Date)
    created_by = Column(String(50))
    updated_by = Column(String(50))
    webhook = Column(String(255))
    
    __table_args__ = (
        CheckConstraint('role_level >= 1 AND role_level <= 5', name='chk_role_level'),
        CheckConstraint('role_level >= 1', name='users_role_level_check'),
        CheckConstraint('status >= 1', name='users_status_check'),
    )