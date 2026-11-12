import pandas as pd
df = pd.DataFrame ({'product':["laptop","mobile","tablet","moniter"],
       'sales':[50000,30000,15000,20000],
       'profit':[8000,5000,2000,3500]})
greater_sales = df[(df['sales'] > 20000) & (df['profit'] > 4000)]
print(greater_sales)