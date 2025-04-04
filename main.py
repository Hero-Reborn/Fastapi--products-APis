from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/product/list", response_model=List[schemas.ProductResponse])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    skip = (page - 1)
    return crud.get_products(db, skip=skip, limit=1)

@app.get("/product/{pid}/info", response_model=schemas.ProductResponse)
def product_info(pid: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add", response_model=schemas.ProductResponse)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.put("/product/{pid}/update", response_model=schemas.ProductResponse)
def update_product(pid: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    updated_product = crud.update_product(db, pid, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product
