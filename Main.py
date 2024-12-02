import fastapi
from fastapi import FastAPI
from Helper import Product
import Helper
import uuid
app = FastAPI()
purchaseList=Helper.purchaseList
@app.post("/receipts/process")
async def add_product(product: Product):
    total=Helper.calculate_points(product)
    unique_id=str(uuid.uuid4())
    while unique_id in purchaseList.keys():
        unique_id=str(uuid.uuid4())
    purchaseList[unique_id]=total
    Helper.purchaseList= purchaseList
    return {"id" :unique_id}
@app.get("/get-message")
async def read_root():
    return {"Message":"Congrats!"}
@app.get("/receipts/{id}/points")
async def get_product_points(id):
    for key in purchaseList.keys():
        if key==id:
            return {"points": purchaseList[id]}
    return {"error":"Id does not exist"}
