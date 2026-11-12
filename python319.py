import pandas as pd
import numpy as np
df = pd.DataFrame({
    'employees': ['a','b','c','d','e'],
    'salary' :[30000,np.nan,45000,50000,np.nan],
    'experience':[2,4,np.nan,5,3]
})
missing_value = df['experience'].isnull()
df['experience'] = df['experience'].fillna(
    df['experience'].median()
)
print(df['experience'],missing_value)
