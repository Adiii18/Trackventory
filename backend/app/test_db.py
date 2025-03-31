from database import SessionLocal

# Test database connection
try:
    db = SessionLocal()
    print("Database connection successful!")
    db.close()
except Exception as e:
    print("Error connecting to the database:", e)
