# Task 1

# Grade Calculator:
# Write a program that calculates and displays the letter grade for
# a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

#input- score - 89

#output- B
'''
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

'''

# If, elif, els

x = int(input("Enter the score: \n"))
'''
if x in range(90, 101):
    print(f"Your Grade is A \t", "And your Mark entered is: ",x)
elif x in range(80, 90):
    print(f"Your Grade is B \t", "And your Mark entered is: ", x)
elif x in range(70, 80):
    print(f"Your Grade is C \t", "And your Mark entered is: ", x)
elif x in range(60, 70):
    print(f"Your Grade is D \t", "And your Mark entered is: ", x)
elif x in range(0, 60):
    print(f"Your Grade is F \t","And your Mark entered is: ", x)
else:
    print("Below par Grade")
'''


# Alternate solution for the above problem

if x >= 90 and x <= 100:
    print(f"Your Grade is A \t", "And your Mark entered is: ", x)
elif x >= 80 and x <= 89:
    print(f"Your Grade is B \t", "And your Mark entered is: ", x)
elif x >= 70 and x <= 79:
    print(f"Your Grade is C \t", "And your Mark entered is: ", x)
elif x >= 60 and x <= 69:
    print(f"Your Grade is D \t", "And your Mark entered is: ", x)
elif x >= 0 and x <= 59:
    print(f"Your Grade is F \t", "And your Mark entered is: ", x)
else:
    print("Mark you entered is out of Range!")



