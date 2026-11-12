import numpy as np
january = np.array([
    [100, 200],
    [300, 400]
])
february =  np.array([
    [500, 600],
    [700, 800]
])
sales_down = np.concatenate((january,february),axis=0)
print(sales_down)
print(np.shape(sales_down))
sales_side = np.concatenate((january,february),axis=1)
print(sales_side)
print(np.shape(sales_side))