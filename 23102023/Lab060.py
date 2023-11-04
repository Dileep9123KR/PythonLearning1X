# Factorial

num = int(input("Enter some number or digits \n"))

sumTotal = 0
while num != 0:
    digit = num % 10
    sumTotal = sumTotal + digit
    num //= 10  # or num = int (num / 10)

print(sumTotal)
