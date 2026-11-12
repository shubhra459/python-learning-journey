import pandas as pd
df = pd.DataFrame({
    'customer': ['Rahul', 'Aman', 'Priya', 'Rahul', 'Sneha'],
    'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Bengaluru'],
    'sales': [5000, 3000, 7000, 8000, 4000]
})
identify_duplicate = df[df["city"].duplicated()]
manager = df.drop_duplicates(subset = 'customer',keep = 'last')
#duplicate = df['city'].drop_duplicates(subset = 'city')
print(identify_duplicate)
print(manager)
#print(duplicate)