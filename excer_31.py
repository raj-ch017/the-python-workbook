"""
Exercise 31: Sum of the digits in an integer

Develop a program that reads a four-digit integer from the user and displays the sum of the
digits in the number. For example, if the user enters 3141 then your program should display:

    3 + 1 + 4 + 1 = 9

"""

the_num = int(input("Please enter a four-digit integer: "))

# removing the first digit of the integer from the left
first_digit = the_num // 1000
num = the_num - (first_digit*1000)

# removing the second digit of the integer from the left
second_digit = num // 100
num = num - (second_digit * 100)

# removing the third digit of the integer from the left
third_digit = num // 10
num = num - (third_digit * 10)  # the fourth digit is the final digit left in the integer

sum = first_digit + second_digit + third_digit + num

print("The digits of {} add up to {}.".format(the_num,sum))

