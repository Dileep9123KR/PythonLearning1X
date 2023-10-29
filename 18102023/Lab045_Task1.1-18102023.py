# Research What is Fibonacci series and Factorial.
# Take an input and print the series.

# Fibonacci Series
# The Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


num = int(input("Enter a number \n"))
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()

# Factorial Series
# A factorial is a mathematical operation that you write like this: n!
# It represents the multiplication of all numbers between 1 and n
# if no is 5 factorial is

x = int(input("Enter a number \n"))
if x < 0:
    print("Factorial is possible")
else:
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    print("Factorial is :", fact)
