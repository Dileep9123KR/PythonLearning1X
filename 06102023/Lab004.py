# Take input from a user to make a simple calculator
"""
num 1 + num 2
num 1 - num 2
num 1 * num 2
num 1 / num 2
"""
num1 = (input("Enter Sample number \n"))
print(type(num1))  # Here num1 treat as a string

num1 = int(input("Enter first number \n"))
num2 = int(input("Entre second number \n"))
print(type(num1))  # Here num1 treat as an integer
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)