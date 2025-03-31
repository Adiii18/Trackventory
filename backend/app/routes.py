from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Product
from schemas import ProductCreate
import crud

app = FastAPI()

@app.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)
