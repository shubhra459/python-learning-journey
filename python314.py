import numpy as np
data = np.genfromtxt(
    "marks.txt",
    missing_values= "NA",
    filling_values= 0
)    
average = np.mean(data)
print(average)