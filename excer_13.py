"""
Exercise 13: Making Change

Consider the software that runs on a self-checkout machine. One task that it must be able to
perform is to determine how much change to provide when the shopper pays for a purchase with cash.

Write a program that begins by reading a number of cents from the user as an integer. Then your
program should compute and display the denominations of the coins that should be used to give that amount of change to the shopper. The change should be given using as few coins as possible.

Assume that the machine is loaded with pennies, nickels, dimes, quarters, loonies and toonies.

"""

# penny - 1 cent
# nickels - 5 cents
# dime - 10 cents
# quarters - 25 cents
# loonies - 1 dollar
# toonies - 2 dollars

cents_count = int(input("Enter the change amount in cents: "))

penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200

# for toonie
num_t = cents_count // toonie
print("{} toonies".format(num_t))
cent_r = cents_count % toonie

# for loonie
num_l = cent_r // loonie
print("{} loonies".format(num_l))
cent_r1 = cent_r % loonie

# for quarters
num_q = cent_r1 // quarter 
print("{} quarter".format(num_q))
cent_r2 = cent_r1 % quarter

# dime
num_d = cent_r2 // dime
print("{} dimes".format(num_d))
cent_r3 = cent_r2 % dime

# nickel
num_n = cent_r3 // nickel
print("{} nickels".format(num_n))
cent_r4 = cent_r3 % nickel

# penny
num_p = cent_r4 // penny
print("{} pennies".format(num_p))
cent_r5 = cent_r4 % penny


