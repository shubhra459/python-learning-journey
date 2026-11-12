import numpy as np
sales = np.array([100,150,120,180])
percentage_growth = np.diff(sales)/ sales[:-1]*100
print(percentage_growth)