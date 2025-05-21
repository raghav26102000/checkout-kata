from models.product import Product
from services.checkout import Checkout
from dotenv import load_dotenv
import os

load_dotenv()

def get_catalog():
    return {
        'A': Product(name='A', unit_price=int(os.getenv("A_UNIT")), discount_qty=int(os.getenv("A_DISCOUNT_QTY")), discount_price=int(os.getenv("A_DISCOUNT_PRICE"))),
        'B': Product(name='B', unit_price=int(os.getenv("B_UNIT")), discount_qty=int(os.getenv("B_DISCOUNT_QTY")), discount_price=int(os.getenv("B_DISCOUNT_PRICE"))),
        'C': Product(name='C', unit_price=int(os.getenv("C_UNIT"))),
        'D': Product(name='D', unit_price=int(os.getenv("D_UNIT"))),
    }

if __name__ == "__main__":
    checkout = Checkout(get_catalog())
    items = input("Scan items (e.g., AAABBD): ").strip().upper()

    try:
        for item in items:
            checkout.scan(item)
        print("Total: Rs", checkout.total())
    except ValueError as e:
        print(e)