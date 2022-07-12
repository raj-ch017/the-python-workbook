"""
Exercise 15: Distance Units

In this exercise, you will create a program that begins by reading a measurement in feet from 
the user. Then your program should display the equivalent distance in inches, yards and miles.

Use the internet to look up the necessary conversion factors if you don't have them memorized.

"""

# 1 feet = 12 inches
# 1 feet = 0.333 yards
# 1 feet = 0.000189394 mile

num_feet = float(input("Enter a distance in feet: "))

num_inches = num_feet * 12
print("{} feet = {} inches".format(num_feet,num_inches))

num_yard = num_feet * 0.333
print("{} feet = {} yards".format(num_feet,num_yard))

num_mile = num_feet * 0.000189394
print("{} feet = {} miles".format(num_feet,num_mile))