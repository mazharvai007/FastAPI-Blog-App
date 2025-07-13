from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from repositories.user import UserRepository
from schemas.user import UserCreate, UserView
from schemas.auth import Token

from db.session import get_db
from utils.jwt_manager import create_access_token, create_refresh_token, verify_token

router = APIRouter()


@router.post("", response_model=UserView)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    user_repo = UserRepository(db=db)
    existing_user = user_repo.get_user_by_email(email=payload.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists!"
        )

    new_user = user_repo.create_user(email=payload.email, password=payload.password)

    return UserView(id=new_user.id, email=new_user.email, is_active=new_user.is_active)


# Route for getting token (login)
@router.post("/token", response_model=Token)
async def login_for_access_token(
    from_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = UserRepository(db=db).get_user_for_token(
        email=from_data.username, password=from_data.password
    )
    token_subject = {"sub": str(user.id)}
    access_token = create_access_token(data=token_subject)
    refresh_token = create_refresh_token(data=token_subject)

    return {"access_token": access_token, "refresh_token": refresh_token}


# Router for refresh token
@router.post("/refresh", response_model=Token)
async def refresh_access_token(refresh_token: str, db: Session = Depends(get_db)):
    payload = verify_token(refresh_token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token"
        )

    payload_subject = payload.get("sub")
    user = UserRepository(db=db).get_user_by_id(id=payload_subject)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found!"
        )

    token_subject = {"sub": str(user.id)}
    new_access_token = create_access_token(data=token_subject)
    new_refresh_token = create_refresh_token(data=token_subject)

    return {"access_token": new_access_token, "refresh_token": new_refresh_token}
