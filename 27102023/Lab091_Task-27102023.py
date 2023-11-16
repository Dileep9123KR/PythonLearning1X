# 1. Write a Python program to find the largest number in a list.

list1 = [10, 25, 30, 15, 55, 13]
op = max(list1)
print("The maximum num is :", op)

# 2. Write a Python program to find the smallest number in a list.
op1 = min(list1)
print("The smallest num is :",op1)


# 3. Write a Python program to sum all numbers in a list.
op2 = sum(list1)
print("Sum of the list is :", op2)

# 4. Write a Python program to multiply all numbers in a list.
newList = [2,3,4,5]

def multiplyList(myList):
    result = 1
    for i in myList:
        result = result * i
    return result

print("After multiplication :", multiplyList(newList))


# 5. Write a Python program to count the number of strings in a list
# where the string length is 2 or more and the first and last character are the same.
def count_strings(list_str):
    ctr = 0
    for i in list_str:
        if len(i) > 2 and i[0] == i[-1]:
            ctr += 1
    return ctr

list_str = ["sample", "test", "strings", "strategies"]
for i in list_str:
    a = count_strings(list_str)

print(a)
