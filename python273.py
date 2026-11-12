import numpy as np
sales = np.array([120,250,180,300,90,450,200])
total_sales = np.sum(sales)
average = np.mean(sales)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
greater_200 = np.sum(sales>200)
print(total_sales, average, highest_sales, lowest_sales, greater_200)