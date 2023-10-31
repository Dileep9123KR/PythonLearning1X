# Functions - Block of codes
# 1. Built-in functions :- which are created by python for us so that we can use it without
# creating any new ones by our own
# 2. Custom functions :- You can create a function which is a block of code that anyone can use it.


# a = int(input("Enter a num \n"))
# b = int(input("Enter b num \n"))
#
# print("Sum is = ",a+b)

def sum(a,b):
    return a+b


a = int(input("Enter a num \n"))
b = int(input("Enter b num \n"))
print("Sum is =",sum(a,b))

print(sum(23,20))

# after a bunch of line of codes, call the same function sum()

print(sum(25, 35))

