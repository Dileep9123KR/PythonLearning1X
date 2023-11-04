# Trying palindrome with function
# Reverse the string and match with the old string
# two methods can be used
#           1. By using a traditional method
#           2. by using built-in functions

# 1. By using a traditional method

def reverse_string(input_string):  # consider input string is ABCD
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str


original_string = "ABA"
rev_str = reverse_string(original_string)
print(rev_str)

if original_string == rev_str:
    print("It's a Palindrome")
else:
    print("Sorry.! Not a Palindrome")

