import numpy as np
department = np.array([
    "Sales",
    "HR",
    "Sales",
    "Analytics",
    "HR",
    "Sales",
    "Analytics",
    "Sales"
])
departments_unique ,department_counts = np.unique(department,return_counts=True)
print(departments_unique,department_counts)

