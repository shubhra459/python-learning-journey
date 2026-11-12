import numpy as np
revenue = np.array([5000,np.nan,7000,6000,np.nan,8000])
missing_value = np.isnan(revenue)
clean_revenue = np.nan_to_num(revenue, nan=0)
print(missing_value,clean_revenue)
