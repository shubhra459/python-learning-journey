import numpy as np
scores = np.array([75,82,91,68])
np.savetxt("scores.txt",scores)
store = np.loadtxt("scores.txt").astype(int)
print(store)