"""
Exercise 34: Even or Odd?

Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.

"""

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("{} is even.".format(num))
else:
    print("{} is odd.".format(num))

