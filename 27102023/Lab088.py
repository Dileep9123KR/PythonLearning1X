# scope of the function: the value for num is will be thw same in outside of the function

num = 5

def mutliply_by_5(n):
    n *= 5
    num = n
    print("Value of num inside fun :", num)
    return n


result = mutliply_by_5(num)
print(result)
print("Value of num outside fun :", num)