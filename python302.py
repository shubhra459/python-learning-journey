import numpy as np
statuses = np.array([
    "Verified", "Pending", "Rejected",
    "Verified", "Processing", "Pending"
])
print(np.isin(statuses,["Pending","Rejected"]))