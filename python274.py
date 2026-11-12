import numpy as np
sales = np.array([150,320,80,450,220,90,380,170])
greater_250 = (sales[sales>=250])
total = np.sum(greater_250)
total_day = np.sum(sales>=250)
print(total, total_day)
