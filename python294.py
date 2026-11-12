import numpy as np
sales =  np.array([
    [120, 150, 135, 180],
    [200, 190, 220, 210],
    [90, 110, 85, 130]
])
total_sum = np.sum(sales ,axis =1)
monthly_total = np.sum(sales,axis = 0)
highest_total = np.argmax(monthly_total)
max_sales = np.max(monthly_total)
index = np.argmax(total_sum)
diffrence = np.diff(monthly_total)
percentage = diffrence / monthly_total[:-1]*100
highest_percentage = np.argmax(percentage)
print(percentage[highest_percentage])
print(percentage)
print(diffrence)
print(index)
print(total_sum)
print(total_sum[index])
print(monthly_total)
print(highest_total)
print(max_sales)