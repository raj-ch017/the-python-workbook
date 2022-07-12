"""
Exercise 19: Free Fall

Create a program that determines how quickly an object is travelling when it hits the ground.

The user will enter the height from which the object is dropped in meters (m). Because the 
object is dropped with its initial speed is 0m/s. 

Assume that acceleration due to gravity is (9.8) m/s^2. You can use the formula:
    
    velocity_final = ((initial_velocity) ** 2 + 2 * a * d)**(1/2)

to compute the final speed, when the initial speed, acceleration (a), and distance (d) are known.

"""

a = 9.8

height = float(input("Enter the height from which the object is dropped: "))

v_f = round((2 * a * height) ** (0.5),1)

print("The final velocity of the object dropped from {} m is {} m/s.".format(height,v_f))

