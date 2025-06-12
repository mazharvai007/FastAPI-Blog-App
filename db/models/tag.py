from db.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    tag_name = Column(String(255), index=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
