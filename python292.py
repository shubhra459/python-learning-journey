import numpy as np
sales = np.array([100,150,120,180,90,220,160])
average = np.mean(sales)
greater = sales[(sales>average)]
indices = np.where(sales>average)
maximum_sales= np.max(sales)
maximum_indices = np.argmax(sales)
print(maximum_sales,maximum_indices)
print(average,greater,indices)