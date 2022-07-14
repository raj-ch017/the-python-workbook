"""
Exercise 40: Name That Triangle

A triangle can be classified based on the lengths of its side as equilateral, isosceles or 
scalene. All 3 sides of an equilateral triangle have the same length. An isosceles triangle 
has two sides that are the same length, and a third side that is a different length.
If all the sides have different lengths, then the triangle is a scalene.

Write a program that reads the length of 3 sides of a triangle from the user. Display a 
message indicating the type of the triangle.

"""

sideA = float(input("Enter the side length 1 of triangle: "))
sideB = float(input("Enter the side length 2 of triangle: "))
sideC = float(input("Enter the side length 3 of triangle: "))

if sideA == sideB == sideC:
    print("The triangle is: Equilateral")
elif sideA == sideB or sideA == sideC or sideB == sideC:
    print("The triangle is: Isosceles")
else:
    print("The triangle is: Scalene")

    