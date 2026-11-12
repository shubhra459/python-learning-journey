import numpy as np
marks = np.array([35,48,72,29,90])
result = np.where((marks >= 40) ,"pass","fail")
print(result)