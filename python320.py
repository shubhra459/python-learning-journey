import pandas as pd
import numpy as np
df = pd.DataFrame({
    'customer': ['Rahul', 'Aman', 'Priya', 'Sneha', 'Rohit'],
    'age': [22, 25, np.nan, 28, 30],
    'email': ['rahul@gmail.com', np.nan, 'priya@gmail.com',
              'sneha@gmail.com', np.nan],
    'city': ['Delhi', 'Mumbai', 'Bengaluru', 'Pune', 'Delhi']
})
remove = df.dropna(subset= 'email')
print(remove)