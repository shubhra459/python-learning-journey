import numpy as np
spending = np.array([500, 1200, 750, 3000, 450, 1800])
result= np.where(
    spending >= 1000,
    "premium",
    "regular"
)
print(result)