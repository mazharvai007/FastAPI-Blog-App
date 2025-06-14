from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from slugify import slugify
import time
from schemas.user import UserView


class BlogCreate(BaseModel):
    title: str
    content: str
    is_active: bool = False
    slug: Optional[str] = None

    @classmethod
    def create_slug(cls, title: str):
        # Automatically generate a slug from the title
        __slugify = slugify(title)
        __time_hash = hash(time.time())  # time hashed
        return f"{__slugify}-{__time_hash}"  # Added hashed time with the title slug for uniqueness

    # Override the __init__ method to automatically generate the slug
    def __init__(self, **data):
        super().__init__(**data)
        if self.title:
            self.slug = self.create_slug(self.title)


class BlogRead(BaseModel):
    id: int
    slug: str
    author_id: int
    created_at: datetime
    author: UserView

    class Config:
        from_attributes = True


class BlogPagination(BaseModel):
    total_count: int
    skip: int
    limit: int
    data: List[BlogRead]

    class Config:
        from_attributes = True
