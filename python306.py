import numpy as np
prices = np.array([100,250,300,450,500,650])
updated_prices=np.delete(prices,[1,4])
print(prices)
print(updated_prices)