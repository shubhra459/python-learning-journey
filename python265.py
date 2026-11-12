import numpy as np
online_sales = np.array([120,150,200])
store_sales = np.array([180,220,250])
all_sales = np.concatenate((online_sales,store_sales))
print(all_sales)