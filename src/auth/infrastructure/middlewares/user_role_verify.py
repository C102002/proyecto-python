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
            raise HTTPException(status_code=404, detail="User not found")
                
        if not set(scopes.scopes).intersection(set(decoded["scopes"])):
            raise HTTPException(status_code=403, detail="Forbidden: Client attempts to access admin endpoint.")
        
        user=res.value

        return {
            "user_id":   user.id.user_id,
            "email":     user.email.email,
            "scopes":    decoded["scopes"]
        }