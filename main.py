from fastapi import Depends,FastAPI
from models import Product
from database import session
from database import engine
from sqlalchemy.orm import Session

import database_models


app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)  # Create tables in the database

products = [
    Product(id=1, name="Product 1", description="Description 1", price=10.99, quantity=100),
    Product(id=2, name="Product 2", description="Description 2", price=20.99, quantity=50),
    Product(id=3, name="Product 3", description="Description 3", price=30.99, quantity=25), 
    Product(id=4, name="Product 4", description="Description 4", price=40.99, quantity=10) 
]

def initialize_database():
    db = session()
    if(db.query(database_models.Product).count()) == 0:  # Clear existing data
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()
    db.close()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()    

initialize_database()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(database_models.Product).filter(database_models.Product.id == id).first()

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    db.refresh(database_models.Product)
    return database_models.Product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    
    if not db_product:
        return {"message": "Product not found"}
    
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    
    if not db_product:
        return {"message": "Product not found"}
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}