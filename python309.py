import numpy as np
scores = np.array([75,82,91,68])
np.save("scores.npy",scores)
loaded_scores = np.load('scores.npy')
print(loaded_scores)