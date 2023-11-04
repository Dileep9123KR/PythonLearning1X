# Using lambda expression for palindrome

original_str = "Dileep"
reverse_str = lambda original_str : original_str [::-1]

if reverse_str("Dileep") == original_str:
    print("It's a Palindrome")
else:
    print("Not a palindrome")


