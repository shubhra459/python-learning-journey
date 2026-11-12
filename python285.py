import numpy as np
ads = np.array([20,25,30,35])
sales = np.array([100,150,200,250])
result = np.cov(ads,sales)
print(result[0,1])