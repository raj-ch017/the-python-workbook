"""
Exercise 32: Sort 3 integers

Create a program that reads three integers from the user and displays them in sorted order
(from smallest to largest).
Use the [min] and [max] functions to find the smallest and largest values. The middle value
can be found by computing the sum of all three values, and the subtracting the minimum and
the maximum value.

"""

first_int = int(input("Please enter an integer of your choice: "))
second_int = int(input("Please enter the second integer of your choice: "))
third_int = int(input("Please enter the third integer of your choice: "))

max_val = max(first_int,second_int,third_int)
min_val = min(first_int,second_int,third_int)

s = first_int + second_int + third_int
mid_val = s - (max_val + min_val)

print("Here are the integers your entered: {}, {} and {}".format(first_int,second_int,third_int))
print("Here are the integers in ascending order: {}, {}, {}".format(min_val,mid_val,max_val))

