# Factorial
# By using Loop

number = int(input(" Please enter a number \n"))
if number < 0:
    print("Factorial is not possible.!")
else:
    fact = 1
    for a in range (1, number+1):
        fact = fact * a

print("Factorial is : ", fact)


