# Break and Continue with the loops
# break is used to escape the loop when the condition is not met.

count = 1
while count <= 10:
    print(count)
    if count >= 5:
        break
    count = count + 1


for counter in range(1, 10):
    if counter == 5:
        break
    print(counter)

print("This is where for loop is finished")

