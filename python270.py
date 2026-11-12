import numpy as np
sales = np.array([500,200,800,100])
names = np.array(["rahul","amit","priya","neha"])
order = np.argsort(sales)
print(names[order[::1]])
print(np.argsort(sales))