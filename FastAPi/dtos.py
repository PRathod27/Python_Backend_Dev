from pydantic import BaseModel

class ProductDTO(BaseModel):
    id:int
    title:str
    name: str
    description: str
    price :float = 0.00

