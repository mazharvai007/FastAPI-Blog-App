from pydantic import BaseModel, Field
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException, status


# Properties required during user creation
# Request Body/Schema/Payload
class UserCreate(BaseModel):
    """Request Body/Schema/Payload"""

    email: str
    password: str = Field(..., min_length=4)

    def __init__(self, **data):
        super().__init__(**data)

        if self.email:
            try:
                email_info = validate_email(self.email, check_deliverability=False)

                self.email = email_info.normalized

            except EmailNotValidError as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="Not a valid email!"
                )


# Response Body/Payload/Schema
class UserView(BaseModel):
    """Response Body/Payload/Schema"""

    id: int
    email: str
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        from_attributes = True
