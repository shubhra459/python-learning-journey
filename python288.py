import numpy as np

sales = np.array([
    [120, 150, 135, 180],
    [200, 190, 220, 210],
    [90,  110, 85,  130]
])
total = np.sum(sales,axis=1)
highest_sales = np.argmax(total)
print(highest_sales)
q1 = np.percentile(sales,25)
q3 = np.percentile(sales,75)
iqr = q3 - q1
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr
outlier = sales[(sales<lower)|(sales>upper)]
print(outlier)
changes = np.diff(sales,axis=1)
print(changes)
correlarion = np.corrcoef(sales[0],sales[1])[0,1]
print(correlarion)
daily_sales = np.array([120,80,150,60,200])
indices = np.where(daily_sales>100)
print(indices)