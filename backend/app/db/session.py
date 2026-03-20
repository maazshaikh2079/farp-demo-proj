from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from app.core.config import settings


# 1. Create the engine using the dynamic DATABASE_URL from our settings
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True  # vital for production to handle dropped connections
)

# 2. Create a session factory
# This creates a "SessionLocal" class that will generate new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Database Dependency
# This is used in your FastAPI routes to inject a database session
def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get a database session for a request.
    Ensures the session is closed after the request is finished.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
