from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="Product 1", description="Description 1", price=10.99, quantity=100),
    Product(id=2, name="Product 2", description="Description 2", price=20.99, quantity=50)
]

@app.get("/")
def welcome():
    return {"message": "Welcome to the FASTAPI backend!"}

@app.get("/products")
def get_all_products():
   return products
