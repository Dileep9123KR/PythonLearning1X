# Task 2
# Right Triangle Star Pattern
# *
# **
# ***
# ****
# *****


tri = int(input("Enter the number of rows to be displayed\n"))

for i in range(0,tri):
    for j in range(0, i+1):
        print("*",end="")
    print()


