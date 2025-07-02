from src.auth.infrastructure.repositories.query.orm_user_query_repository import OrmUserQueryRepository
from ..database.postgres.postgres_database import PostgresDatabase

class GetOrmUserRepository:
    
    async def __call__(self):
        session_generator = PostgresDatabase().get_session()
        session = await anext(session_generator)
        orm_repository = OrmUserQueryRepository(session)
        return orm_repository