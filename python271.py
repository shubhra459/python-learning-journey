import numpy as np
sales = np.array([120,250,180,300,90,450,200])
gerater_than_200 = (sales>200)
print(f"total sales {np.sum(sales)}\n average sales {np.mean(sales)}\n highest sale {np.max(sales)}\n lowest sales {np.min(sales)}")
print(sales[gerater_than_200])