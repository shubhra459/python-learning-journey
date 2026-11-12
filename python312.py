import numpy as np
with open ("data.txt","w") as file:
    file.write("10\n20\nNA\n40")
data1 = np.genfromtxt(
    "data.txt",
    missing_values="NA",
    filling_values=-1
)
print(data1)