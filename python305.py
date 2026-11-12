import numpy as np
sales = np.array([250,800,450,1200,600,300])
print(np.extract(sales > 500,sales))
print(np.extract((sales < 300)|(sales > 800),sales))