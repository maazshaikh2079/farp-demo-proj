from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator
from sqlalchemy.orm import Session

from app.core.config import settings


# 1. Create the engine using the dynamic DATABASE_URL from our settings
# pool_pre_ping=True is vital for production to handle dropped connections
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

# 2. Create a session factory
# This creates a "SessionLocal" class that will generate new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Database Dependency
# This is used in your FastAPI routes to inject a database session
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
