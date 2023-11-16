# Subset

set1 = {1,2,3,4,5,6}
set2 = {7,8,9,10}
#subset = set2.issubset(set1)
subset = set1.issubset(set2)
print(subset)

print("\n")
t1 = set(["TestingAcademy", "Good", "For", "PythonLearning", "TestingAcademy"])
print(t1)

for i in t1:
    print(i)

print("\n")

t2 = set([1,2,3,4,5,6,7,8,9,10,11,12])
print(t2)
t2.remove(5)
print("After performing remove (5): ", t2)