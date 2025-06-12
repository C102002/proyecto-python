from sqlmodel import Field, SQLModel
from pydantic import EmailStr
from ...domain.enum.user_role_enum import UserRoleEnum

class User(SQLModel, table=True):
    id: str = Field(nullable=False, primary_key=True, unique=True)
    email: EmailStr = Field(nullable=False, unique=True, index=True)
    name: str = Field(nullable=False)
    password: str = Field(nullable=False)
    role: UserRoleEnum = Field(default=UserRoleEnum.CLIENT)