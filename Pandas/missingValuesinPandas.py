import pandas as pd

df = pd.read_csv('LifeExpectancyData.csv')
print(df)

print(df.info)
print(df.isnull)
