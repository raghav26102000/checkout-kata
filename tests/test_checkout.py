import pytest
from models.product import Product
from services.checkout import Checkout

@pytest.fixture
def checkout():
    catalog = {
        'A': Product(name='A', unit_price=50, discount_qty=3, discount_price=130),
        'B': Product(name='B', unit_price=30, discount_qty=2, discount_price=45),
        'C': Product(name='C', unit_price=20),
        'D': Product(name='D', unit_price=15),
    }
    return Checkout(catalog)

@pytest.mark.parametrize("items,expected", [
    ("", 0),
    ("A", 50),
    ("AB", 80),
    ("CDBA", 115),
    ("AA", 100),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAA", 230),
    ("AAAAAA", 260),
    ("AAAB", 160),
    ("AAABB", 175),
    ("AAABBD", 190),
    ("DABABA", 190),
])
def test_checkout_total(checkout, items, expected):
    for item in items:
        checkout.scan(item)
    assert checkout.total() == expected