# List is a collection which is ordered and changeable. Allows duplicate members.
listTest = ["1", "2", 3]
for data in listTest:
    print(data)
# add item into the list
listTest.append("new item")

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

tupleTest = ("1", "2", "3")
print("data for tuple")
for data in tupleTest:
    print(data)


# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
thisset.add("apple")
for data in thisset:
    print(data)
