from fastapi import Depends, HTTPException
from fastapi.security import SecurityScopes
from ..roles.role_scopes import ALL_KNOWN_SCOPES, ROLE_SCOPES
from .jwt_transformer import JwtTransformer
from ..database.postgres.postgres_database import PostgresDatabase
from src.auth.infrastructure.repositories.query.orm_user_query_repository import OrmUserQueryRepository
from .get_orm_user_repository import GetOrmUserRepository

class UserRoleVerify:

    def __init__(self, user_query_repository: OrmUserQueryRepository = Depends(GetOrmUserRepository())):
        self.user_query_repository = user_query_repository


    async def __call__(self, scopes: SecurityScopes, user_email: str = Depends(JwtTransformer())):
        user = await self.user_query_repository.get_user_email(user_email)

        if user.is_error:
            raise HTTPException(status_code=404, detail="User not found")
        
        roles = ALL_KNOWN_SCOPES[user.value.role]
        
        if not any(scope in roles for scope in scopes.scopes):
            raise HTTPException(status_code=403, detail="Not enough permissions")

        return user_email