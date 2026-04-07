from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserCreateRequest(BaseModel):
    email: EmailStr
    username: str

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    is_active: bool