import jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
from core.config import settings


# Create Access Token
def create_access_token(
    data: dict,
    exipres_delta: Optional[timedelta] = settings.ACCESS_TOKEN_EXPIRE_MINUTES,
):
    """
    Create Access Token
    """

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=exipres_delta)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


# Create Refresh Token
def create_refresh_token(
    data: dict,
    expires_delta: Optional[timedelta] = settings.REFRESH_TOKEN_EXPIRE_MINUTES,
):
    """
    Create Refresh Token
    """

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


# Verify Token
def verify_token(token: str):
    """
    Verify Token
    """

    try:
        payload: jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError as e:
        print(e)
    except jwt.PyJWKError as e:
        print(e)

    return None
