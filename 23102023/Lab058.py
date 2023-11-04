# Trying palindrome with function
# Reverse the string and match with the old string
# two methods can be used
#           1. By using a traditional method
#           2. by using built-in functions


# 2. by using built-in functions

original_string = str(input("Enter a word \n"))

def isPalindrome(original_string):
    rev_str = original_string[::-1]  # list slicing method [Starting point:Ending point:Step]
    print(rev_str)
    if original_string == rev_str:
        print("It's a Palindrome.!")
    else:
        print("Sorry.! Not a Palindrome")


print(isPalindrome(original_string))