import numpy as np
approved_ids = np.array([101, 103, 105, 107])
incoming_orders = np.array([101, 102, 105, 108, 107, 110])
print(~np.isin(incoming_orders,approved_ids))