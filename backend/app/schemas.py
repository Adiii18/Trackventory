from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 🛒 Product Schema
class ProductBase(BaseModel):
    name: str
    category: Optional[str] = None
    price: float  # Selling price
    cost: float   # Purchase cost
    stock: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Helps with ORM mode in SQLAlchemy

# 📦 Purchase Schema
class PurchaseBase(BaseModel):
    product_id: int
    quantity: int
    cost: float  # Cost per unit

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseResponse(PurchaseBase):
    id: int
    purchase_date: datetime

    class Config:
        from_attributes = True

# 💰 Sale Schema
class SaleBase(BaseModel):
    product_id: int
    quantity_sold: int
    sale_price: float
    profit: float

class SaleCreate(SaleBase):
    pass

class SaleResponse(SaleBase):
    id: int
    sale_date: datetime

    class Config:
        from_attributes = True

# 👤 User Schema
class UserBase(BaseModel):
    username: str
    role: str  # Enum: 'admin', 'manager', 'staff'

class UserCreate(UserBase):
    password: str  # Plain text, will be hashed

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
