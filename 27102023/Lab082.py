# Set is an unordered collections of data types

set1 = set()
print(set1)

set2 = set("Dileep")  # ordered collection
print(set2)

set3 = {1, 2, 3, 4, 5}
print(type(set3), set3)

set4 = {1, 1, 2, 2, 4, 2, 5, 2}  # no duplicate values allowed, latest value will be shown here
print(set4)  # output => {1, 2, 4, 5}

#set4[3] = 3  # Not possible to change, immutable
print(set4)


set1 = set(["Dileep", "Dilu", "Dileep"])
print(set1)