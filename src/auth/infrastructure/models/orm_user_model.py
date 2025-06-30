from sqlmodel import Field, SQLModel
from ...domain.enum.user_role_enum import UserRoleEnum

class OrmUserModel(SQLModel, table=True):

    __tablename__ = "user" # type: ignore

    id: str = Field(nullable=False, primary_key=True, unique=True)
    email: str = Field(nullable=False, unique=True, index=True)
    name: str = Field(nullable=False)
    password: str = Field(nullable=False)
    role: UserRoleEnum = Field(default_factory=lambda: UserRoleEnum.CLIENT)

    def create_user(self, id: str, email: str, name: str, password: str, role: UserRoleEnum) -> "OrmUserModel":
        return OrmUserModel(
            id=id,
            email=email,
            name=name,
            password=password,
            role=role
        )