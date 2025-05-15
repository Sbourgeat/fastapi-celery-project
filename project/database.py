from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from project.config import settings


engine = create_engine(
    settings.DATABASE_URL, connect_args=settings.DATABASE_CONNECT_DICT
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()