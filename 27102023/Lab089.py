list1 = [5, 10, 15, 20, 25]
print("At starting : ", list1)


def mult_by10(myList):
    myList[0] *= 10
    myList[1] *= 10
    myList[2] *= 10
    myList[3] *= 10
    myList[4] *= 10


print("Outside function :", list1)
mult_by10(list1)  # here function called with list1
print(list1)  # the output values are changed, due to mutable nature of the list


# trying the same with tuple
print("\n")
tuple1 = (5, 10, 15, 20, 25)
print("At starting : ", tuple1)

def mult_by10(mytuple):   # tuple is immutable so changing will not affect
    mytuple[0] *= 10
    mytuple[1] *= 10
    mytuple[2] *= 10
    mytuple[3] *= 10
    mytuple[4] *= 10

print("Outside function :", tuple1)
mult_by10(tuple1)
print(tuple1)