from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional
from utils.jwt_manager import verify_token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from db.base import User
from utils.password_manager import PasswordManager
from db.session import get_db

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/auth/token"
)  # this '/auth/token' will be the token api or endpoint


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

    # Get User by its ID
    def get_user_by_id(self, id: int) -> Optional[User]:
        """
        Get User by its ID
        """

        return self.db.query(User).filter(User.id == id, User.is_active == True).first()

    # Get user for token
    def get_user_for_token(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(email=email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials!"
            )

        is_password_matched = PasswordManager.verify_password(password, user.password)

        if not is_password_matched:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials!"
            )

        return user

    # Current user execution
    @staticmethod
    def get_current_user(
        token: str = Depends(oauth2_schema), db: Session = Depends(get_db)
    ):
        payload = verify_token(token)

        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token!"
            )

        user = db.query(User).filter(User.id == payload.get("sub")).first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_UNAUTHORIZED, detail="User not found!"
            )

        return user
