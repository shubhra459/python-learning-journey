import numpy as np 
scores = np.array([60,70,90,100])
updated_scores = np.insert(scores,2,[75,80])
new_scores = np.append(scores,[110,120])
print(updated_scores)
print(new_scores)