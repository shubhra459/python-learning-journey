import numpy as np
sales = np.array([8,12,20,30,40,60])
lower = 10
upper = 50
outlier = sales[(sales<lower) | (sales>upper)]
print(outlier)