from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.product import Product
from services.checkout import Checkout
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Checkout Kata API")

class ScanRequest(BaseModel):
    items: str

def get_catalog():
    return {
        'A': Product(name='A', unit_price=int(os.getenv("A_UNIT")), discount_qty=int(os.getenv("A_DISCOUNT_QTY")), discount_price=int(os.getenv("A_DISCOUNT_PRICE"))),
        'B': Product(name='B', unit_price=int(os.getenv("B_UNIT")), discount_qty=int(os.getenv("B_DISCOUNT_QTY")), discount_price=int(os.getenv("B_DISCOUNT_PRICE"))),
        'C': Product(name='C', unit_price=int(os.getenv("C_UNIT"))),
        'D': Product(name='D', unit_price=int(os.getenv("D_UNIT"))),
    }

@app.post("/checkout")
def checkout_items(request: ScanRequest):
    checkout = Checkout(get_catalog())
    try:
        for item in request.items.upper():
            checkout.scan(item)
        return {"total": checkout.total()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))