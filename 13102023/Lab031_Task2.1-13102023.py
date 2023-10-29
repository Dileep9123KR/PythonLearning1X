# Task #2.1

# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)
radius = float (input("Please enter the radius of the circle: \n"))
print("Area = ", 3.14 * radius**2, end='\n')

# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.
number1 = input("Enter your first number: \n")
number2 = input("Enter your second number: \n")
'''
if number1 > number2:
    print(number1,"is greater than ", number2)
elif number1 < number2:
    print(number1,"is less than ", number2)
else:
    print(number1,"is equal to", number2)
'''
if number1 < number2:
    print(number1,"is less than", number2)
elif number1 > number2:
    print(number1,"is greater than", number2)
else:
    print(number1,"equal to ", number2)