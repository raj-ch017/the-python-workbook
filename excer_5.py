"""
Exercise 5: Bottle Deposits

In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one litre or
less have a $0.10 deposit, and drink containers holding more than one litre have a 
$0.25 deposit.

Write a program that reads the number of containers of each size from the user. 
Your program should continue by computing and displaying the refund that will be received
for returning those containers. Format the output so that it includes a dollar sign
and always displays exactly two decimal places.
"""

print("Type A: Bottles with volume 1 litre or less")
print("Type B: Bottles with volume more than 1 litre")
print()


in_litre = int(input("Enter the number of Type A containers: "))
in_morelitre = int(input("Enter the number of Type B containers: "))

refund_a = round(in_litre * 0.10, 2)
print("Refund for Type A containers: ${}".format(refund_a))

refund_b = round(in_morelitre*0.25, 2)
print("Refund for Type B containers: ${}".format(refund_b))

