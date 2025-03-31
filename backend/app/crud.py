from sqlalchemy.orm import Session
from models import Product, Purchase, Sale, User
from schemas import ProductCreate, ProductUpdate  # Define Pydantic schemas

# Create Product
def create_product(db: Session, product: ProductCreate):
    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        cost=product.cost,
        stock=product.stock
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Get All Products
def get_products(db: Session):
    return db.query(Product).all()

# Get Product by ID
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# Update Product
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

# Delete Product
def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
