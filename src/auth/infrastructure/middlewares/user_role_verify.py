from fastapi import Depends, HTTPException
from fastapi.security import SecurityScopes
from src.common.infrastructure import GetPostgresqlSession
from .jwt_transformer import JwtTransformer
from ..repositories.query.orm_user_query_repository import OrmUserQueryRepository
from sqlalchemy.ext.asyncio import AsyncSession

class UserRoleVerify:

    async def __call__(self, scopes: SecurityScopes, decode_token: dict = Depends(JwtTransformer()), postgres_session: AsyncSession = Depends(GetPostgresqlSession())):

        user_query_repository = OrmUserQueryRepository(postgres_session)

        user = await user_query_repository.get_user_email(decode_token["sub"])
        print(decode_token["scopes"])
        print(scopes.scopes)
        if user.is_error:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not set(scopes.scopes).intersection(set(decode_token["scopes"])):
            raise HTTPException(status_code=403, detail="Not enough permissions")

        return decode_token["sub"]