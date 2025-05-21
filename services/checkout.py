import logging
from collections import Counter
from models.product import Product
from typing import Dict, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Checkout:
    def __init__(self, product_catalog: Dict[str, Product]):
        self.catalog = product_catalog
        self.scanned_items: List[str] = []

    def scan(self, item: str):
        if item in self.catalog:
            self.scanned_items.append(item)
            logger.info(f"Scanned item: {item}")
        else:
            logger.warning(f"Unknown item: {item}")
            raise ValueError(f"Unknown item scanned: {item}")

    def total(self) -> int:
        total = 0
        item_counts = Counter(self.scanned_items)
        logger.debug(f"Item counts: {item_counts}")

        for item, count in item_counts.items():
            product = self.catalog[item]
            if product.discount_qty and product.discount_price:
                groups = count // product.discount_qty
                remainder = count % product.discount_qty
                subtotal = groups * product.discount_price + remainder * product.unit_price
                logger.info(f"{item}: {groups} discount groups, {remainder} at unit price = Rs{subtotal}")
                total += subtotal
            else:
                subtotal = count * product.unit_price
                logger.info(f"{item}: {count} × {product.unit_price} = Rs{subtotal}")
                total += subtotal

        logger.info(f"Total checkout price: Rs{total}")
        return total