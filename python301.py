import numpy as np
spending = np.array([300,800,1500,2500,4500,1200,600])
result = np.select (
   [ spending < 500,
    (spending >= 500) & (spending < 2000),
    spending >= 2000
   ],
   ["low","medium","high"],
   default="unknown"
) 
print(result)