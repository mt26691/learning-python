# set contains unique item only
sampleSet = {1, 3, 4}

sampleList = [1,1,2,3]

convertedSet = set(sampleList)

for data in convertedSet:
    print(data)

# we can add element to the set
sampleSet.add(5)

if 5 in sampleSet:
    print("5 is in set")

# find intersection between set
set1 = {"1","2","3"}
set2 = {"2","3"}
interset = set1 & set2
print(interset)

