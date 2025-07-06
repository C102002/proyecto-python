from ..database.postgres.postgres_database import PostgresDatabase

class GetPostgresqlSession:
    
    async def __call__(self):
        temp_db_instance = PostgresDatabase() 
    
        async with temp_db_instance.get_session() as session: 
            yield session