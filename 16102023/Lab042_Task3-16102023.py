# Task 3
# Triangle Classifier:

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).

# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

x = int(input("Enter side1 : \n"))
y = int(input("Enter side2 : \n"))
z = int(input("Enter side3 : \n"))

if x == y and y == z and x == z:
    print("This is an Equilateral Triangle")
elif (x == y) and (x == z):
    print("This is a Isosceles Triangle")
else:
    print("This is a Scalene Triangle")

