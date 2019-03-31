listExample = ["1", "2", "3"]
print(listExample)
for data in listExample:
    print(data)
if "1" in listExample:
    print("1 is exist in the list")

print(len(listExample))
print("append data to the list")
listExample.append("test")
print(listExample[3])
#To add an item at the specified index, use the insert() method:
listExample.insert(1,"inserted data")
for data in listExample:
    print(data)

listExample.append("1")

listExample.remove("1")

print("after removing 1")
for data in listExample:
    print(data)

#the clear method is used for empty the list

listExample.clear()

print("list len " + str(len(listExample)))