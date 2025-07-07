from fastapi import Depends, HTTPException
from fastapi.security import SecurityScopes
from src.common.infrastructure import GetPostgresqlSession
from .jwt_transformer import JwtTransformer
from ..repositories.query.orm_user_query_repository import OrmUserQueryRepository
from sqlalchemy.ext.asyncio import AsyncSession

class UserRoleVerify:
    async def __call__(self,
                       scopes: SecurityScopes,
                       decoded: dict = Depends(JwtTransformer()),
                       db: AsyncSession = Depends(GetPostgresqlSession())):

        repo = OrmUserQueryRepository(db)
        res  = await repo.get_user_email(decoded["sub"])
        if res.is_error:
            raise HTTPException(404, "User not found")

        user = res.value  # supongamos que aquí tienes tu modelo con .id, .email, etc.

        # comprobación de scopes…
        if not set(scopes.scopes).intersection(decoded["scopes"]):
            raise HTTPException(403, "Forbidden")

        return {
            "user_id":   user.id.user_id,
            "email":     user.email.email,
            "scopes":    decoded["scopes"]
        }
