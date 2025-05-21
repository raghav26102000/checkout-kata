from dataclasses import dataclass
from typing import Optional

@dataclass
class Product:
    name: str
    unit_price: int
    discount_qty: Optional[int] = None
    discount_price: Optional[int] = None