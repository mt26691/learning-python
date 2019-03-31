import pandas as pd

df = pd.read_csv("sample.csv")

# find data in second row and first column
print(df.ix[1,0])
print(df.iloc[1,0])
print("****************************")
print(df.head())

data = [1, 2, 3, 4, 5]
df1 = pd.DataFrame(data)
print(df1)

data2 = {"Name": ["Tom", "Jack", "Steve", "Ricky"], "Age": [28, 34, 29, 42]}
df2 = pd.DataFrame(data2)
print(df2)

dataFrame = pd.DataFrame({"a": [1, 2, 3], "b": ["4", "5", "6"]})
print(dataFrame.head(2))
print(dataFrame["a"])