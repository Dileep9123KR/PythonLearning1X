# Map and Filter in List

numbers = [1,2,3,4,5]
# need to print the squares the numbers in List
sq = lambda x: x * x
sq_numbers = []
for i in numbers:
    sq_numbers.append(sq(i))

print(sq_numbers)

# printing the same squares in list by using map function and only in single line of code

sq_numbers2 = list(map(lambda x: x * x, numbers))

print(sq_numbers2)

# map can take any functions

def triple(a):
    return a * 3

triple_numbers = list(map(triple, numbers))
print(triple_numbers)
