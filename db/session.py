from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)  # Remove echo from production


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# This generator is responsible to give our database session to work with database
def get_db():
    try:
        db_session = SessionLocal()
        yield db_session
    finally:
        db_session.close()
 