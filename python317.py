import pandas as pd

df = pd.DataFrame({
    'product': ['Laptop', 'Mobile', 'Tablet', 'Monitor'],
    'sales': [50000, 30000, 15000, 20000],
    'profit': [8000, 5000, 2000, 3500]
})
sort_values = df.sort_values(by = 'profit',ascending= True)
print(sort_values)