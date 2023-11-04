# Task 1
# Count vowels and consonants in a String
# aeiou
# input = pramod
# vowels = 2
# a, e, i, o, u . Consonants are the rest of the letters in the
# alphabet: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y and z .
# The letter y is a bit different, because sometimes it acts as a consonant and sometimes it acts as a vowel.

word = str(input("Enter a sentence \n"))

vowels = 0
consonants = 0

for i in word:
    if i =='a' or i == 'A' or i =='e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("The number of vowels are :", vowels)
print("The number of consonants are :", consonants)
