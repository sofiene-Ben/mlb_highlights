from sqlmodel import  create_engine, Session, SQLModel, select
from typing import Optional
from fastapi import Depends
from typing import Annotated
import os
from app.domain.entities.Users import Users
from app.infrastructure.config.app import settings

postgres_url = settings.database_url

if not postgres_url:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = create_engine(
    postgres_url,
    pool_size=10,  # Taille du pool de connexions
    max_overflow=20,  # Nombre maximum de connexions supplémentaires
    pool_timeout=30,  # Temps d'attente avant d'abandonner
    echo=True
    )

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def get_user(db_session: Session, username: str) -> Optional[Users]:
    statement = select(Users).where(Users.username == username)
    user = db_session.exec(statement).first()
    return user