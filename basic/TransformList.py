minutes = [1, 2, 3]
secs = [data * 60 for data in minutes]
for data in secs:
    print(data)

lower = ["nguyen", "manh", "tung"]
upper = [data.upper() for data in lower]

for data in upper:
    print(data)

testString = "tung,xzc,za"
stringArray = testString.strip().split(",")

for data in stringArray:
    print(data)