from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_router
from app.db.session import engine
from app.db.base_class import Base
# OR  from app.models.product import Base
# OR  from app.models.product import Product as DBProduct
from app.core.config import settings


# 1. Create database tables at startup
Base.metadata.create_all(bind=engine)
# OR  DBProduct.metadata.create_all(bind=engine)

# 2. Initialize the FastAPI app with settings from core/config.py
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 3. Top-level Health Check (Useful for Docker/Kubernetes)
@app.get("/", tags=["Health"])
def health_status():
    """Endpoint to verify the API is running correctly."""

    return {"status": "Healthy"}


# 4. Include the bundled API router using the global prefix
# Final URLs: http://localhost:8000/api/v1/products/
app.include_router(api_router, prefix=settings.API_V1_STR)
