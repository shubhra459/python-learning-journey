import numpy as np
sales =  np.array([100, 110, 120, 115, 130, 125, 500])
q1 = np.percentile(sales,25)
q3 = np.percentile(sales,75)
iqr = q3 - q1
upper = q3 + iqr*1.5
lower = q1 - iqr*1.5
print(upper)
outlier = sales[sales>upper]
print(outlier)
outlier1 = sales[(sales<lower)|(sales>upper)]
print(outlier1)