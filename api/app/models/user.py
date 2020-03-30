from sqlalchemy import Column, Integer, String, DateTime

from app.models.db_base import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    phone = Column(String(32), nullable=False, index=True, unique=True)
    name = Column(String(100), default='', nullable=False)
    pwd = Column(String(100), nullable=False)
    create_time = Column(DateTime, nullable=False)
    email = Column(String(50), index=True, unique=True, nullable=False)
    avatar = Column(String(50), default='', nullable=False)
    introduction = Column(String(255), default='', nullable=False)
