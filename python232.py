import pandas as pd
data = {
"name": ["rahul","don","don mohan","billa","gaurav"],
"age": [21,34,56,28,97],
"marks": [23,45,36,78,29],
"department":["sales","hr","analytics","marketing","analytics"]
}
df = pd.DataFrame(data)
sorted_df = df.sort_values('marks',ascending=False)
sorted_df1 = df.sort_values('age')
print(sorted_df)
print(sorted_df1)