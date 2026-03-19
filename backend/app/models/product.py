from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base

class Product(Base):
    """
    SQLAlchemy model for the 'products' table.
    Inherits from the central Base class in app.db.base_class.
    """

    __tablename__ = "products"

    # 'mapped_column' provides better type hinting for your IDE
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), index=True, nullable=False)

    description: Mapped[str] = mapped_column(String(500), nullable=True)

    price: Mapped[float] = mapped_column(Float, nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, default=0)
