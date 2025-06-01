from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()

class PostgresDatabase:
    def __init__(self):
        self.url = os.getenv("DATABASE_URL")

        if self.url is None:
            raise ValueError("La variable de entorno DATABASE_URL no esta definida")
        
        self.engine = create_engine(self.url, echo=True)

    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> Generator[Session, None, None]:
        with Session(self.engine) as session:
            yield session