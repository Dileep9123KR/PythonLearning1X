# Union and intersection and difference

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
b_set = set1.union(set2)
print(b_set)

# intersection
set3 = {2, 3, 4, 6, 7}
set4 = {4, 5, 7, 8, 9, 10}
c_set = set3.intersection(set4)
print(c_set)

# difference

set5 = {4, 7, 8, 9, 6}
set6 = {4, 9, 10, 2, 3}
a_set = set5.difference(set6)
d_set = set6.difference(set5)
print(a_set)
print(d_set)
