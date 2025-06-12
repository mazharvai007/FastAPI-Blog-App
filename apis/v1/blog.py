from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.blog import Blog
from db.session import get_db
from repositories.blog import BlogRepository
from schemas.blog import BlogCreate, BlogRead

from schemas.blog import BlogPagination

router = APIRouter()


# Post route
@router.post("", response_model=BlogRead)
def create_blog(payload: BlogCreate, db: Session = Depends(get_db)) -> Blog:
    blog_repo = BlogRepository(db=db)

    # TODO - We need dynamic author id and category id
    new_blog = blog_repo.create_blog(blog=payload, author_id=2, category_id=1)
    return new_blog


# Get route
@router.get("", response_model=BlogPagination)
def get_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    blog_repo = BlogRepository(db=db)
    blogs = blog_repo.get_blogs(skip=skip, limit=limit)
    return blogs
