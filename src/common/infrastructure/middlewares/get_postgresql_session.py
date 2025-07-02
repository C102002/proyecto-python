from ..database.postgres.postgres_database import PostgresDatabase

class GetPostgresqlSession:
    
    async def __call__(self):
        session_generator = PostgresDatabase().get_session()
        session = await anext(session_generator)
        return session