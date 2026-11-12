import numpy as np
ratings = np.array([5, 4, 5, 3, 2, 5, 4, 3, 5, 2, 4, 5])
counts = np.unique(ratings,return_counts=True)
highest_frequency = np.max(ratings)
print(counts,highest_frequency)