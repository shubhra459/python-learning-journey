import numpy as np
sales = np.array([120, 150, 90, 200, 175, 220, 160])
highest_sales = np.argmax(sales)
human_day =highest_sales + 1
sales_value = np.max(sales[highest_sales])
print(sales_value)
print(human_day)
