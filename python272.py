import numpy as np
sales = np.array([150,320,80,450,220,90,380,170])
total_sales = np.sum(sales)
atleast_200 = (sales[sales>=200])
avg = np.mean(atleast_200)
print(total_sales,atleast_200,avg)