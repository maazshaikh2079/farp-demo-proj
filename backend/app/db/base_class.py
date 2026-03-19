from sqlalchemy.orm import DeclarativeBase

# Modern SQLAlchemy 2.0 style
# This is the central "registry" for all your database tables
class Base(DeclarativeBase):
    pass
