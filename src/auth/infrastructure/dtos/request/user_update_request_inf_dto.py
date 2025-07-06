from pydantic import BaseModel, Field, EmailStr

class UserUpdateRequestInfDto(BaseModel):
    id: str = Field(..., description="User ID")
    email: EmailStr | None = Field(description="User email", default=None)
    name: str | None = Field(description="User name", default=None)
    password: str | None = Field(description="User password", default=None)

    class Config:
        extra = "forbid"