from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from slugify import slugify
import time
from schemas.user import UserView


# Read Category
class CategoryRead(BaseModel):
    id: int
    slug: str
    author_id: int
    created_at: datetime
    author: UserView

    class Config:
        from_attributes = True


# Create category slug
class CreateCategory(BaseModel):
    category_name: str
    slug: Optional[str] = None

    @classmethod
    def create_slug(cls, name: str):
        """
        Automatically generated a slug from category name

        slugify = create slug based on the category name
        time_hash = create hashed time for unique class

        return = return a unique slug
        """
        __slugify = slugify(name)
        __time_hash = hash(time.time())

        return f"{__slugify}-{__time_hash}"

    # Override the __init__ method to automatically generated the slug
    def __init__(self, **data):
        super().__init__(**data)

        if self.category_name:
            self.slug = self.create_slug(self.category_name)
