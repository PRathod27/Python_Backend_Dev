from fastapi import FastAPI
from products import ProductsData
from dtos import ProductDTO

app = FastAPI()

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



@app.post("/createproduct")
def create_product(data:ProductDTO):
    product_data = data.model_dump()
    print(product_data)

    return {"status":"Created Succesfully"}


#pydantic used for validation
@app.put("/updateproduct/{product_id}")
def update_product(data:ProductDTO, product_id:int):

    for index, oneProduct in enumerate(ProductsData):
        if (oneProduct.get("id")==product_id):
            ProductsData[index] = data.model_dump()
            return {"status" : "Product updated succesfully", "product" : ProductsData}
    
    return {"error":"Product not found..."}


@app.delete("/delete_product/{product_id}")
def deleteProduct(product_id:int):
    for index, oneProduct in enumerate(ProductsData):
        if oneProduct.get("id") == product_id:
            deleted_product = ProductsData.pop(index)  
            return {"status":"Product Deleted Successfully", "product":deleted_product}
        
        return {"status":"Error Occurred"}
