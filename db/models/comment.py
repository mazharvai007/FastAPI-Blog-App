from sqlalchemy import Column, ForeignKey, Integer, Text
from db.base import Base


class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    comment_text = Column(Text)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
