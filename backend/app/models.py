from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from database import Base  # Import your database connection

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100))
    price = Column(DECIMAL(10,2), nullable=False)
    cost = Column(DECIMAL(10,2), nullable=False)
    stock = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    cost = Column(DECIMAL(10,2), nullable=False)
    purchase_date = Column(TIMESTAMP, server_default=func.current_timestamp())

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity_sold = Column(Integer, nullable=False)
    sale_price = Column(DECIMAL(10,2), nullable=False)
    profit = Column(DECIMAL(10,2), nullable=False)
    sale_date = Column(TIMESTAMP, server_default=func.current_timestamp())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum("admin", "manager", "staff"), nullable=False)
