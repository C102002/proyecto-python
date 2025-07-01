from pydantic import BaseModel, EmailStr, Field
from src.auth.domain.enum.user_role_enum import UserRoleEnum

class UserRegisterRequestInfDto(BaseModel):
    email: EmailStr = Field(...)
    name: str = Field(...)
    password: str = Field(...)
    role: UserRoleEnum = Field(...)