"""
Exercise 12: Distance Between Two Points on Earth

The surface of the Earth is curved, and the distance between degrees of longitude varies
with latitude. As a result, finding the distance between two points on the surface of the Earth is more complicated than simply using the Pythagorean Theorem.

Let (t1,g1) and (t2,g2) be the latitde and longitude of two points on the Earth's surface. 
The distance between these points, following the surface of the Earth, in kilometers is:

    distance = 6371.01 * arccos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cost(g1 - g2))

Create a program that allows the user to enter the latitude and longitude of two points on
the Earth in degrees. Your program should display the distance between these points, following
the surface of the Earth, in kilometers.

"""
import math

lat_A = float(input("Enter the latitude of point A (in degrees): "))
long_A = float(input("Enter the longitude of point A (in degrees): "))

lat_B = float(input("Enter the latitude of point B (in degrees): "))
long_B = float(input("Enter the longitude of point B (in degrees): "))

# (lat_A,long_A) and (lat_B,long_B) are the two points

lat_radA = math.radians(lat_A)
long_radA = math.radians(long_A)

lat_radB = math.radians(lat_B)
long_radB = math.radians(long_B)

term1 = math.sin(lat_radA) * math.sin(lat_radB)
term2 = math.cos(lat_radA) * math.cos(lat_radB) * math.cos(long_radA - long_radB)

distance = 6371.01 * math.acos(term1 + term2)

print("The distance between ({},{}) deg and ({},{}) deg is {} km".format(lat_A,long_A,lat_B,long_B,round(distance,2)))


# Coordinates of London: (51,0.12)
# Coordinates of New York: (40,74)
# Distance: 5637.51 km