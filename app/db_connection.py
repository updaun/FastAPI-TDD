import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DEV_DATABASE_URL = os.getenv("DEV_DATABASE_URL")

engine = create_engine(DEV_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        