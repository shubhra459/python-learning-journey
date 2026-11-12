import numpy as np
data = np.genfromtxt("studentss.txt")
print(data[(data>150) &(data < 300) ])


data1 =np.array([45,80,25,90,60])
print(np.where(data1 > 50)[0])