import numpy as np
sales = np.array([100, 200, 150, 300, 400])
cumsum = np.cumsum(sales)
indices = np.where([cumsum>=700][0])
first_index =indices[0]
number = first_index + 1
print(number)
print(first_index)