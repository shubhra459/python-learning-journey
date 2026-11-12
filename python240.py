import pandas as pd
data = { 
    "name": ["rahul", "don", "billa", "don", "gaurav", "billa"],
    "age": [21, 34, 28, 34, 25, 28],
    "marks": [78, 65, 90, 65, 82, 90]
}
df = pd.DataFrame(data)
cleaned_df = df.drop_duplicates()
print(cleaned_df)