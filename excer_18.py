"""
Exercise 18: Volume of a Cylinder

The volume of a cylinder can be computed by multiplying the area of its circular base by 
height. Write a program that reads the radius of a cylinder, along with it's height, from
the user and computes its volume. Display the result rounded to one decimal place.

"""

import math

pi = math.pi 

radius = float(input("Enter the radius of the cylinder: "))
area = pi * (radius ** 2)

height = float(input("Enter the height of the cylinder: "))

volume = round(height * area,2)

print("The volume of a cylinder with radius {} unit and height {} unit is {} cube unit".format(radius,height,volume))

