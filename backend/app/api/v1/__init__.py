from fastapi import APIRouter
from app.api.v1.endpoints import products

# Create the v1 router
api_router = APIRouter()

# Include individual endpoint routers
# All product routes will now start with /products
api_router.include_router(products.router, prefix="/products", tags=["products"])

# Future endpoints would go here:
# api_router.include_router(users.router, prefix="/users", tags=["users"])
