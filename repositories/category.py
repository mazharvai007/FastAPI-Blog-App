from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schemas.category import CreateCategory
from db.base import Category


class CategoryRepository:
    def __init__(self, db: Session) -> None:
        """
        Initialize session
        """
        self.db = db

    # Create Category
    def create_category(self, category: CreateCategory, author_id: int):
        """
        Create new category in the database
        """

        db_category = Category(
            category_name=category.category_name,
            slug=category.slug,
            author_id=author_id,
        )

        try:
            self.db.add(db_category)
            self.db.commit()
            self.db.refresh(db_category)
        except IntegrityError as e:
            print(e)
            self.db.rollback()
            raise HTTPException(status_code=404, detail="Something went wrong")

        return db_category
