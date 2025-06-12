from db.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(255), nullable=False, index=True)
    slug = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now)

    author = relationship("User")
