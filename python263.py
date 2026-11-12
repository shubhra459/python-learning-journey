import numpy as np
sales = np.array([
    "Online",
    "Store",
    "Online",
    "Store",
    "Online",
    "Wholesale"
])
channels = np.unique(sales)
print(channels)