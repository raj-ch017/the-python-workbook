"""
Exercise 9: Compound Interest

Pretend that you have just opened a new savings account that earns 4% interest per year.
The interest that you earn is paid at the end of the year, and is added to the balance of
the savings account.

Write a program that begins by reading the amount of money deposited into the account by the 
user. Then your program should compute and display the amount in the savings account after
    
    * 1 year
    * 2 years
    * 3 years

Display each amount so that it is rounded to 2 decimal places.

"""

rate = 0.04

balance = float(input("Enter the amount deposited: "))

balance1 = round(balance + (rate*balance),2)
print("Balance at the end of year one: {}".format(balance1))

balance2 = round(balance1 + (rate*balance1),2)
print("Balance at the end of year two: {}".format(balance2))

balance3 = round(balance2 + (rate*balance2),2)
print("Balance at the end of year three: {}".format(balance3))

