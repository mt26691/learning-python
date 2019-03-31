#Tuples are unordered sequence
sampleTuple = ("1","2","3")
print(sampleTuple[2])
#in python we can use negative index
print(sampleTuple[-3])
print(type(sampleTuple))

#we can slice the tuple
sampleSlicing = ("1","2","3","4")
print(sampleSlicing[0:2])
#tuple is immutable, so we can't change its values
ratings = (1,5,1,2,5)
sortedRatings = sorted(ratings)
for rating in sortedRatings:
    print(rating)

#tuple nesting
sampleNesting = (1,2,("pop, rock"))

#List is mutable
listSample = [1,2,3]
#add new element to the list
listSample.append(4)
#add miltiple element to the list
listSample.extend([4,2,3])

#delete a element from the list
del listSample[1]

# referenceList is reference to list sample, not a clone
referenceList = listSample

cloneList = listSample.copy()