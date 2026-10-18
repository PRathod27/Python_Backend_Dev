from fastapi import FastAPI
from products import ProductsData
from dtos import ProductDTO

app = FastAPI()


@app.post("/createproduct")
def create_product(data:ProductDTO):
    product_data = data.model_dump()
    print(product_data)

    return {"status":"Created Succesfully"}


#pydantic used for validation
