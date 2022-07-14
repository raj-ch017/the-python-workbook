"""
Exercise 39: Sound Levels

The following table lists the sound level in decibels for several common noise

    Name            Decibel level (db)

    Jackhammer          130
    Gas lawnmower       106
    Alarm Clock         70
    Quiet Room          40

Write a program that reads a sound level in decibels from the user. If the user enters a
decibel level that matches one of the noise in the table, then your program should display
a message containing only that noise. 
If the user enters a number of decibels between noises listed then your program should 
display a message indicating which noise the level is between. Ensure that your program
also generates resonable output for a value smaller than the quietest noise in the table,
and for a value larger than the loudest noise in the table.

"""

val_a = 130
val_b = 106
val_c = 70
val_d = 40

in_val = float(input("Enter a noise level (in db): "))

if in_val > val_a:
    print("{} db is louder than a jackhammer.".format(in_val))
elif in_val == val_a:
    print("{} db is as loud as a jackhammer.".format(in_val))
elif in_val < val_a and in_val > val_b:
    print("{} db is quieter than a jackhammer but louder than a gas lawnmower.".format(in_val))
elif in_val == val_b:
    print("{} db is as loud as a gas lawnmower.".format(in_val))
elif in_val < val_b and in_val > val_c:
    print("{} db is quieter than a gas lawnmower but louder than an alarm clock.".format(in_val))
elif in_val == val_c:
    print("{} db is as loud as an alarm clock!".format(in_val))
elif in_val < val_c and in_val > val_d:
    print("{} db is quieter than an alarm clock but louder than quiet room.".format(in_val))
elif in_val == val_d:
    print("{} db is equivalent to a quiet room.".format(in_val))
else:
    print("{} db is quieter than a quiet room!".format(in_val))
