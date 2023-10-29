x = range(1, 10)
print(x)
print(type(x))

x = list(range(1, 10)) # stop at last_value-1
print(x)
print(type(x))

for x in range(1, 10): # stop at last_value-1; output will be :-[1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(x)