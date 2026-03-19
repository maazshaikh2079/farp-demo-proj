from pydantic import BaseModel, ConfigDict
from typing import Optional

# 1. Base logic shared by all schemas
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

# 2. Schema for creating a product (No ID, as DB generates it)
class ProductCreate(ProductBase):
    pass

# 3. Schema for updating (Everything optional to allow partial updates)
class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

# 4. Schema for returning data (Includes the ID)
class ProductOut(ProductBase):
    id: int

    # Pydantic v2 configuration
    model_config = ConfigDict(from_attributes=True)
