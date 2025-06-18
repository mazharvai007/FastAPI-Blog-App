from sqlalchemy import func
from sqlalchemy.orm import Session

# from db.session import get_db

# db = get_db().__next__()

from typing import List, Optional
from db.base import Blog
from schemas.blog import (
    BlogCreate,
    BlogRead,
    BlogPagination,
    BlogSingleRead,
    BlogUpdate,
)
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


class BlogRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    # Create Blog
    def create_blog(self, blog: BlogCreate, author_id: int, category_id: int) -> Blog:
        """Create a new blog in the Database"""

        db_blog = Blog(
            title=blog.title,
            slug=blog.slug,
            content=blog.content,
            is_active=blog.is_active,
            author_id=author_id,
            category_id=category_id,
        )

        try:
            self.db.add(db_blog)
            self.db.commit()
            self.db.refresh(db_blog)
        except IntegrityError as e:
            print(e)
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Something went wrong!")

        return db_blog

    # Get Blogs
    def get_blogs(self, skip: int = 0, limit: int = 100) -> BlogPagination:
        """Retrieve a list of blogs with pagination"""

        # Get the total number of blogs from Blog table
        total_count = self.db.query(func.count(Blog.id)).scalar()
        blogs = self.db.query(Blog).offset(skip).limit(limit).all()

        # Explored
        # total_count = self.db.query(Blog).count()
        # blogs = self.db.query(Blog).offset(skip).limit(limit).all()
        # blogs_data = [BlogRead.from_orm(blog) for blog in blogs]

        return BlogPagination(
            total_count=total_count,
            skip=skip,
            limit=limit,
            data=blogs,
        )

    def get_blog_by_id(self, blog_id: int) -> BlogSingleRead:
        blog = self.db.query(Blog).filter(Blog.id == blog_id).first()

        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found!")

        return blog

    def get_blog_by_slug(self, blog_slug: str) -> BlogSingleRead:
        blog = self.db.query(Blog).filter(Blog.slug == blog_slug).first()

        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found!")

        return blog

    def update_blog(self, blog_id: int, blog: BlogUpdate) -> Optional[Blog]:
        """
        Update an existing blog by it's ID
        """

        db_blog = self.db.query(Blog).filter(Blog.id == blog_id).first()

        if not db_blog:
            raise HTTPException(status_code=404, detail="Blog not found!")

        if blog.title:
            db_blog.title = blog.title
            db_blog.slug = blog.slug

        if blog.content is not None:
            db_blog.content = blog.content

        if blog.is_active is not None:
            db_blog.is_active = blog.is_active

        try:
            self.db.commit()
            self.db.refresh(db_blog)
        except IntegrityError as e:
            print(e)
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Something went wrong!")

        return db_blog

    def delete_blog(self, blog_id: int) -> bool:
        """
        Delete blog by it's ID
        """

        db_blog = self.db.query(Blog).filter(Blog.id == blog_id).first()

        if not db_blog:
            raise HTTPException(status_code=404, detail="Blog not found!")

        try:
            self.db.delete(db_blog)
            self.db.commit()
        except IntegrityError as e:
            print(e)
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Something went wrong!")
