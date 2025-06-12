from db.base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    poster_image = Column(String)
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    author_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    topic_id = Column(Integer, ForeignKey("topics.id"))

    author = relationship("User")
    category = relationship("Category")
