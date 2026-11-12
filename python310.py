import numpy as np
marks = np.array([75, 82, 91])
attendance = np.array([85, 90, 95])
save = np.savez("save_data.npz",marks= marks,attendance = attendance)
data = np.load("save_data.npz") 
print(data["marks"])
print(data["attendance"])