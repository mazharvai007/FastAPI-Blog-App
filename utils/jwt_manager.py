from fastapi import HTTPException, status
from datetime import datetime, timedelta, timezone
from typing import Optional

from jwt import (
    DecodeError,
    ExpiredSignatureError,
    InvalidTokenError,
    PyJWKError,
    decode,
    encode,
)
from core.config import settings


# Create Access Token
def create_access_token(data: dict):
    """
    Create Access Token
    """

    expires_delta: Optional[timedelta] = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    # print(type(settings.SECRET_KEY))
    # print(type(expires_delta))
    # print(type(settings.REFRESH_TOKEN_EXPIRE_MINUTES))

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})

    encoded_jwt = encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )

    return encoded_jwt


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

    return encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


# Verify Token
def verify_token(token: str):
    """
    Verify JWT Token and return the decoded payload if valid.
    Raises HTTPException for any invalid token case.
    """

    if not token or not isinstance(token, str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token is missing or invalid type.",
        )

    if token.count(".") != 2:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Malformed JWT token. Expected 3 parts separated by '.'!",
        )

    try:
        payload = decode(
            token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return payload

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired."
        )

    except DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is not properly encoded or signed.",
        )

    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token!"
        )

    except PyJWKError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Token verification error: {e}",
        )

    return None
