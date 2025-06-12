from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional
from db.base import User
from fastapi import HTTPException
from utils.password_manager import PasswordManager


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    # Get user by email
    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Get user by email

        SELECT * FROM users WHERE email=given_email
        """
        return self.db.query(User).filter(User.email == email).first()

    # create new user
    def create_user(
        self,
        email: str,
        password: str,
        is_active: bool = True,
        is_superuser: bool = False,
    ) -> User:
        """Create new user"""

        # Password Hashed
        _hashed_password = PasswordManager.get_password_hash(password=password)
        db_user = User(
            email=email,
            password=_hashed_password,
            is_active=is_active,
            is_superuser=is_superuser,
        )

        # Store Db User to database
        self.db.add(db_user)

        try:
            self.db.commit()
            self.db.refresh(db_user)  # refresh database session
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Email already registered!")

        return db_user
