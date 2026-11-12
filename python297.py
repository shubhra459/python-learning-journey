import numpy as np
orders = np.array([
    "Electronics",
    "Clothing",
    "Electronics",
    "Beauty",
    "Clothing",
    "Electronics",
    "Beauty",
    "Electronics",
    "Clothing"
])
unique = np.unique(orders,return_counts = True)
print(unique)
