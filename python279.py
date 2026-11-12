import numpy as np
sales = np.array([150,320,80,450,220,90,380,170])
cumsum = np.cumsum(sales)
indices = np.where([cumsum>=1000][0])
first_index = indices[0]
day_number =first_index + 1
print(day_number)
print(cumsum)