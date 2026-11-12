import numpy as np
online_orders = np.array([101, 102, 103, 105, 107])
store_orders = np.array([102, 103, 104, 107, 108])
print(np.intersect1d(online_orders,store_orders),
      np.setdiff1d(online_orders,store_orders),
      np.union1d(online_orders,store_orders))