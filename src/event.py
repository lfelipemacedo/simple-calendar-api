from datetime import datetime

from sqlalchemy import String, DateTime, Column, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "events".upper()

    id = Column(Integer, primary_key=True)
    name = Column(String(20), name="name", nullable=False)
    description = Column(String(500), name="description", nullable=True)
    event_date = Column(DateTime(timezone=True))
    created_date = Column(DateTime(timezone=True))
    updated_date = Column(DateTime(timezone=True))
