from db.base import Base
from sqlalchemy import Boolean, Column, Integer, String


class Topic(Base):
    id = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String(255), unique=True, nullable=True, index=True)
    is_active = Column(Boolean, default=True)
