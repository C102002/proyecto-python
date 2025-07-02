from fastapi import Depends, HTTPException
from fastapi.security import SecurityScopes
from src.common.infrastructure import ALL_KNOWN_SCOPES, ROLE_SCOPES, GetPostgresqlSession
from .jwt_transformer import JwtTransformer
from ..repositories.query.orm_user_query_repository import OrmUserQueryRepository
from sqlalchemy.ext.asyncio import AsyncSession

class UserRoleVerify:

    async def __call__(self, scopes: SecurityScopes, user_email: str = Depends(JwtTransformer()), postgres_session: AsyncSession = Depends(GetPostgresqlSession())):

        user_query_repository = OrmUserQueryRepository(postgres_session)

        user = await user_query_repository.get_user_email(user_email)
        
        if user.is_error:
            raise HTTPException(status_code=404, detail="User not found")
        
        roles = ROLE_SCOPES[user.value.role.role]
        
        if not set(scopes.scopes).issubset(set(roles)):
            raise HTTPException(status_code=403, detail="Not enough permissions")

        return user_email