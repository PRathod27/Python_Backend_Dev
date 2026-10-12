from fastapi import FastAPI, Request
from products import ProductsData

app = FastAPI()

@app.get("/")
def home():
    return "Home Page"

@app.get("/products")
def get_products():
    return ProductsData

# Path Params
@app.get("/products/{product_id}")
def get_products_by_params(product_id:int):

    ## if product available with the id, return product, else return error message

    products = None
    for oneProduct in ProductsData:
        if oneProduct.get("id") == product_id:
            return oneProduct

     
    return {
        "error":"Product not Found"
    }


# Query params
@app.get("/greet")
def greet_user(request:Request):
    query_params = dict(request.query_params)
    return {
        "greet":f"Hello {query_params.get("name")}, your age is {query_params.get("age")}"
    }