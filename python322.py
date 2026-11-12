import pandas as pd
df = pd.read_excel(
    "pandas_retail_practice_workbook.xlsx.xlsx",
    sheet_name="Orders")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
loc = df.loc[10]
loc1 = df.iloc[10]
print(loc)
print(loc1)