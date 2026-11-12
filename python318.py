import pandas as pd
df = pd.DataFrame({
    'category': ['Electronics', 'Clothing', 'Electronics',
                 'Clothing', 'Furniture', 'Furniture'],
    'product': ['Laptop', 'Shirt', 'Mobile', 'Jeans',
                'Chair', 'Table'],
    'sales': [50000, 2000, 30000, 3000, 8000, 12000],
    'profit': [8000, 500, 5000, 700, 1500, 2500]})
group = df.groupby('category').agg({
    'sales': 'sum',
    'profit': 'mean',
})
print(group)