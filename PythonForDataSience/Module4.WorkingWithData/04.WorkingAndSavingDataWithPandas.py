import pandas as pd

df = pd.read_csv("sample.csv")

# find data in second row and first column
print(df["name"].unique())
dfBig = df["age"]>28
dfBig.to_csv("bimbim.csv")
print(df["age"] > 28)

