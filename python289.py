import numpy as np
daily_sales = np.array([120,80,150,60,200])
lowest = np.min(daily_sales)
index = np.argmin(daily_sales)
print(index)
print(lowest)