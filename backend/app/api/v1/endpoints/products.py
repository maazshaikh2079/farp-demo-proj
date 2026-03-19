from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# These imports assume you moved your files to the new folders
from app.schemas.product import ProductCreate, ProductUpdate, ProductOut
from app.db.session import get_db
from app.models.product import Product as DBProduct


router = APIRouter()


@router.get("/", response_model=List[ProductOut])
def get_all_products(db: Session = Depends(get_db)):
    """Fetch all products."""

    return db.query(DBProduct).all()


@router.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
    Fetches a single product by its unique ID.
    Returns a 404 error if the product does not exist.
    """

    # db_product = db.query(DBProduct).filter(DBProduct.id == product_id).first()
    db_product = db.get(DBProduct, product_id)

    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product w/ ID {product_id} not found"
        )

    return db_product


@router.post("/", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product_in: ProductCreate, db: Session = Depends(get_db)):
    """Create a new product."""

    new_product = DBProduct(**product_in.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.put("/{product_id}", response_model=ProductOut)
def update_product(product_id: int, product_in: ProductUpdate, db: Session = Depends(get_db)):
    """Update an existing product."""

    db_product = db.get(DBProduct, product_id)
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product w/ ID {product_id} not found"
        )

    update_data = product_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product


@router.delete("/{product_id}") # , status_code=status.HTTP_204_NO_CONTENT
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Delete a product."""

    db_product = db.get(DBProduct, product_id)
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product w/ ID {product_id} not found"
        )

    db.delete(db_product)
    db.commit()

    # return None   # 204 status code requires no content
    return {"message": f"Product w/ ID {product_id} deleted"}
