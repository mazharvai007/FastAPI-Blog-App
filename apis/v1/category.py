from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.category import Category
from db.session import get_db
from repositories.category import CategoryRepository
from schemas.category import CategoryRead, CreateCategory

router = APIRouter()


# POST route
@router.post("", response_model=CategoryRead)
def create_category(payload: CreateCategory, db: Session = Depends(get_db)):
    category_repo = CategoryRepository(db)

    # TODO - We need dynamic author id
    new_category = category_repo.create_category(category=payload, author_id=2)
    return new_category
