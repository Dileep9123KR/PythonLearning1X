# Task 2.2

# Use the ternary operator to find the maximum of three numbers entered by the user.

num1 = input("Enter your first number: \n")
num2 = input("Enter your second number: \n")
num3 = input("Enter your third number: \n")

if num1 > num2 and num1 > num3:
    print(num1,"is the maximum number you entered", end='\n')
elif num2 > num3 and num2 > num1:
    print(num2, "is the maximum number you entered", end='\n')
else:
    print(num3, "is the maximum number you entered", end='\n')

