# Task 2

# Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
# n = 12345
# sum = 15
# n = 123
# sum = 6

def isSum(n):
    sum = 0
    for num in str(n):
        sum += int(num)
    return sum


n = int(input("Please enter digits to get sum of it : \n"))
print(isSum(n))