from pydantic import BaseModel, EmailStr, Field


# Properties required during user creation
# Request Body/Schema/Payload
class UserCreate(BaseModel):
    """Request Body/Schema/Payload"""

    email: EmailStr
    password: str = Field(..., min_length=4)


# Response Body/Payload/Schema
class UserView(BaseModel):
    """Response Body/Payload/Schema"""

    id: int
    email: EmailStr
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
        # from_attributes = True