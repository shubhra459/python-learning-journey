import numpy as np
marks = np.array([80,90,np.nan,70,100])
mean = np.mean(marks)
clean_mean = np.nanmean(marks)
print(mean,clean_mean )