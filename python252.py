import numpy as np
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(f"{np.sum(data,axis=1)}\n{np.mean(data,axis=0)}\n{np.max(data,axis=1)}\n{np.min(data,axis=0)}")