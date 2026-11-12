import numpy as np
with open ("students.txt",'w') as file:
   file.write("10\n20\nNA\n40")
data = np.genfromtxt(
    "students.txt",
    missing_values="NA",
    filling_values=0
).astype(int)
average = np.mean(data)
print(average)   