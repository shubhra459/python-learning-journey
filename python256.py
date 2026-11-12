import numpy as np
number = np.array([10,20,30,40,50,60,70,80])
reshape = number.reshape(4,2)
print(f"{np.shape(reshape)}\n{np.ndim(reshape)}\n{np.size(reshape)}")