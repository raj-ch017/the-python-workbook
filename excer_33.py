"""
Exercise 33: Day Old Bread

A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60%.

Write a program that begins by reading the number of loaves of day old bread being purchased
by the user.
Then your program should display the regular prices for the bread, the discount because it is
a day old, and the total price. All of the values should be displayed using two decimal places, and the decimal points in all of the numbers should be aligned when resonable values
are entered by the user.

"""

regular_price = 3.49
#discount = round(0.6 * regular_price,2)
actual_price = round(0.4 * regular_price,2)

num = int(input("Enter the number of loaves of bread: "))

total_regular = regular_price * num
total_discount = total_regular * 0.6

print("The regular price is: $%.2f"%(total_regular))
print("The discount obtained: $%.2f"%(total_discount))

total = round(num * actual_price,2)
print("Total amount: $%.2f"%(total))