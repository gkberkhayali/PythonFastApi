from fastapi import FastAPI
from models import Product
from database import session;

app = FastAPI()

products = [
    Product(id=1, name="Product 1", description="Description 1", price=10.99, quantity=100),
    Product(id=2, name="Product 2", description="Description 2", price=20.99, quantity=50),
    Product(id=3, name="Product 3", description="Description 3", price=30.99, quantity=25), 
    Product(id=4, name="Product 4", description="Description 4", price=40.99, quantity=10) 
]

@app.get("/")
def welcome():
    return {"message": "Welcome to the FASTAPI backend!"}

@app.get("/products")
def get_all_products():
   #Get db connection
   #Write the query to get all products
   db = session()
   products = db.query(Product).all()
   return products


@app.get("/get_product_by_id/{id}")
def get_product_by_id(id: int):
    return next((product for product in products if product.id == id), None)  # Return the first product if not found

@app.get("/get_product_by_id_2/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return None  # Return None if not found


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(product: Product):
    for i, p in enumerate(products):
        if p.id == product.id:
            products[i] = product
            return product
    return {"message": "Product not found"}

@app.delete("/product/{id}")
def delete_product(id: int):
    for i, product in enumerate(products):
        if product.id == id:
            del products[i]
            return {"message": "Product deleted"}
    return {"message": "Product not found"}