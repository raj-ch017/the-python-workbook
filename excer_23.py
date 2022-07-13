"""
Exercise 23: Area of a Regular Polygon

A polygon is regular if its sides are all the same length and the angles between all of the
adjacent sides are equal. The area of a regular polygon can be computed using the following
formula, where (s) is the length of a side and (n) is the number of sides:

    area = [(n) * (s)**2] / 4 * tan(pi/n)

Write a program that reads (s) and (n) from the user and then displays the area of a regular
polygon constructed from these values.

"""

import math

pi = math.pi

length = float(input("Enter the length of the polygon: "))

num = int(input("Enter the number of sides: "))

numerator = (num) * ((length) ** 2)
denominator = 4 * math.tan(pi/num)

area = round(numerator/denominator,2)

print("The area of regular polygon with {} sides and length {} unit is {} square unit".format(num,length,area))

