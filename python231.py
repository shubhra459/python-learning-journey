import pandas as pd
data = {
"name": ["rahul","don","don mohan","billa","gaurav"],
"age": [21,34,56,28,97],
"marks": [23,45,36,78,29],
"department":["sales","hr","analytics","marketing","analytics"]
}
df = pd.DataFrame(data)
sorted_df = df.sort_values('marks')
print(sorted_df)
