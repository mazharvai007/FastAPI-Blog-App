from pydantic import BaseModel


# Auth Token
class Token(BaseModel):
    """
    Auth Token:

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    """

    access_token: str
    refresh_token: str
    token_type: str = "bearer"
