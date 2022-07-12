"""
Exercise 16: Area and Volume

Write a program that begins by reading a radius, r, from the user. The program will continue
by computing and displaying the area of a circle with radius (r) and the volume of a sphere
with radius (r). Use the pi constant in the math module in your calculations. 

"""

# area of circle = pi * r ^ 2
# volume of a sphere = 4/3 * pi * r ^ 3

import math

r = float(input("Enter the radius of the circle: "))

pi = math.pi

area = round(pi * (r**2),2)
print("The area of the circle with radius {} unit is {} square unit.".format(r,area))

volume = round((4/3) * pi * (r**3),2)
print("The volume of a sphere with radius {} unit is {} cube unit.".format(r,volume))