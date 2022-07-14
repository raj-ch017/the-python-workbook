""" 
Exercise 37: Name that Shape

Write a program that determines the name of a shape from its number of sides. Read the number
of sides from the user and then report the appropriate name as part of a meaningful message.
Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
If a number of sides outside of this range is entered then your program should display 
an appropriate error message.

"""

side = int(input("Enter the number of sides: "))

if side < 3:
    print("Error! Invalid input!")
elif side == 3:
    print("{}-sided shape: Triangle".format(side))
elif side == 4:
    print("{}-sided shape: Quadrilateral".format(side))
elif side == 5:
    print("{}-sided shape: Pentagon".format(side))
elif side == 6:
    print("{}-sided shape: Hexagon".format(side))
elif side == 7:
    print("{}-sided shape: Heptagon".format(side))
elif side == 8:
    print("{}-sided shape: Octagon".format(side))
elif side == 9:
    print("{}-sided shape: Nonagon".format(side))
elif side == 10:
    print("{}-sided shape: Dodecagon".format(side))
else:
    print("Error! Input value exceeded domain.")