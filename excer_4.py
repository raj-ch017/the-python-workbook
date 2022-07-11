"""
Exercise 4: Area of a Field

Create a program that reads the length and width a farmer's field 
from the user in feet.
Display the area of the field in acres.
"""

in_length = float(input("Enter the length of the field (in ft): "))
in_width = float(input("Enter the width of the field (in ft): "))

area_ft = in_length * in_width # calculated in feet

# 1 acre = 43560 square feet

area_acre = round(area_ft / 43560, 3)

print("Area of the field is {} acres.".format(area_acre))



