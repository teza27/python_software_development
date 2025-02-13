from functools import reduce
sales_data = [
    {"product": "Apple", "quantity": 5, "price": 2.5},
    {"product": "Banana", "quantity": 10, "price": 1.75},
    {"product": "Orange", "quantity": 8, "price": 3.0},
    {"product": "Grapes", "quantity": 3, "price": 4.25},
    {"product": "Mango", "quantity": 6, "price": 2.0},
]
filtered = reduce(lambda x, y : x + y, list(map(lambda sales: sales["quantity"] * sales["price"], list(filter(lambda data : data["product"] != "Grapes", sales_data)))))
print(filtered)