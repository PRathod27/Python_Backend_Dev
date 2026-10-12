from fastapi import FastAPI
from products import ProductsData

app = FastAPI()

@app.get("/home")
def home():
    return "Home Page"

@app.get("/products")
def get_products():
    return ProductsData