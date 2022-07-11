"""
Exercise 7: Sum of the First n Positive Integers

Write a program that reads a positive integer, n, from the user and then displays
the sum of all the integers from 1 to n. 
The sum of the first n positive integers can be computed using the formula:

            sum = (n(n+1))/2

"""

num = int(input("Enter a positive integer: "))

s = (num * (num+1)) / 2

print("The sum of integers from 1 to {} is {}".format(num,int(s)))

