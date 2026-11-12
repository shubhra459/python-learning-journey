import pandas as pd
data = {
    "name": ['rahul',"don",'billa','gaurav'],
    "age":[21,None,28,None,],
    "marks":[78,65,None,82]
}
df = pd.DataFrame(data)
print(df['age'].fillna(df['age'].mean()))

