from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from db.base import Base


class UserBlogLike(Base):
    __tablename__ = "users_blog_likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    created_at = Column(DateTime, default=datetime.now)
