import numpy as np
ads = np.array([100,200,300,400,500])
sales = np.array([500,400,300,200,100])
result = np.corrcoef(ads,sales)
print(result[0,1])