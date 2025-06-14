from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.blog import Blog
from db.session import get_db
from repositories.blog import BlogRepository
from schemas.blog import BlogCreate, BlogRead, BlogSingleRead

from schemas.blog import BlogPagination

router = APIRouter()


# Crate blog post from this route
@router.post("", response_model=BlogRead)
def create_blog(payload: BlogCreate, db: Session = Depends(get_db)) -> Blog:
    blog_repo = BlogRepository(db=db)

    # TODO - We need dynamic author id and category id
    new_blog = blog_repo.create_blog(blog=payload, author_id=2, category_id=1)
    return new_blog


# Get single blog post by blog_id from this route
@router.get("/{blog_id}", response_model=BlogSingleRead)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    blog_repo = BlogRepository(db=db)
    blog = blog_repo.get_blog_by_id(blog_id=blog_id)
    return blog


# Get all blog post from this route
@router.get("", response_model=BlogPagination)
def get_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    blog_repo = BlogRepository(db=db)
    blogs = blog_repo.get_blogs(skip=skip, limit=limit)
    return blogs
