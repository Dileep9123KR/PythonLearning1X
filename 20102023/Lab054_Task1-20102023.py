# Task 1

# Palindrome Checker:
# Create a function that checks if a given string is a palindrome (reads the same forwards and backward). 121
#
# Example - pramod
# madam - reverse(madam) -> same
# Naman -> reverse -> same
# Malayalam
#
# Compare String with the Reverse of the string

def isPalindrome(p):
    return p == p[::-1]


p = str(input("Enter a string or a name or a word \n"))

answer = isPalindrome(p)
if answer:
    print("Yes, it is a Palindrome.!")
else:
    print("Not a palindrome")


def reverse(s): # by using str reverse
    str1 = ""
    for i in s:
        str1 = i + str1
    return str1
s = str(input("Enter a word \n"))

print("The reverse of the word is -> ", reverse(s), end="")


