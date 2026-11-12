import pandas as pd
data = {
"name" : ["rahu","suman","billa","piyush","prakash"],
"age":  [20,21,23,24,25],
"marks" :[40,50,39,59,10]
}
df = pd.DataFrame(data)
 #print(df[["name","marks"]])

condition = (df["age"]<22) | (df["marks"]>55)
print(df[condition])