
import pandas as pd 
import plotnine as p9

df=pd.read_csv(r"D:\Data\New folder\data-bQxjs.csv")
df.columns
print(df)
for x in range(len(df.columns)):
    print(df.iat[0,x])
    print(df.iat[0,x])

df['avg'] = df.mean(axis=1)

print(df[['X.1','avg']])

