from pydantic import BaseModel, EmailStr, Field

class UserRegisterRequestInfDto(BaseModel):
    email: EmailStr = Field(...)
    name: str = Field(...)
    password: str = Field(...)

    class Config:
        extra = "forbid"