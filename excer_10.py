""" 
Exercise 10: Arithmetic

Create a program that reads two integers, a and b, from the user. 

Your program should compute and display:

    * The sum of a and b
    * The difference when b is subtracted from a
    * The product of a and b
    * The quotient when a is divided by b
    * The remainder when a is divided by b
    * The result of log10 (a)
    * The result of (a) raised to power (b)

"""

import math

a = int(input("Please enter an integer: "))
b = int(input("Please enter another integer: "))

# operation 1 - sum
c = a + b
print("The sum of {} and {} is {}".format(a,b,c))

# operation 2 - difference (a-b)
d = a - b
print("The difference when {} is subracted from {} is {}".format(b,a,d))

# operation 3 - product
e = a * b
print("The product of {} times {} is {}".format(a,b,e))

# operation 4 - quotient of a divided by b
f = a / b
print("The quotient of dividing {} by {} is {}".format(a,b,f))

# operation 5 - remainder of a divided by b
g = a % b
print("The remainder of dividing {} by {} is {}".format(a,b,g))

# operation 6 - log base 10 of (a)
h = math.log(a,10)
print("The result of log base 10 of {} is {}".format(a,h))

# operation 7 - a raised to power (b)
i = a ** b
print("Raising {} to the power {} is {}".format(a,b,i))

