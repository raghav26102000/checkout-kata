# Checkout Kata - Supermarket Pricing

## 🛒 Description
This is a simple checkout system written in Python. It calculates the total price of items scanned, applying group discounts where applicable.

## ✅ Features
- Clean OOP-based architecture
- MVC-inspired structure
- Configurable product catalog
- Discount logic for bulk pricing
- Fully tested with `pytest`

## 🚀 How to Run
```bash
python main.py
```

## 🧪 Run Tests
```bash
pip install pytest
pytest
```

## 🧱 Project Structure
checkout_kata/
├── models/               # Product model (dataclass)
├── services/             # Core checkout logic
├── tests/                # Unit tests with pytest
├── api/                  # FastAPI REST interface
├── main.py               # CLI entry point
├── README.md             # This file
└── requirements.txt      # Dependencies

## 🔧 Technologies Used
- Python 3.9+
- OOP + Clean Architecture
- Pytest for testing

## 🧠 Bonus Steps (If You Have Time)
- Add `FastAPI`/`Django` layer to expose an API for scanning and checking out.
- Use `.env` or config file for pricing rules.
- Add logging/debug modes with the `logging` module.