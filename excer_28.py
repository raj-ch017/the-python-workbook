"""
Exercise 28: Wind Chill

When the wind blows in cold weather, the air feels even cooler than it actually is because
the movement of the air increases the rate of cooling for warm objects, like people.

In 2001, Canada, the United Kingdom and the United States adopted the following formula for
computing the wind chill index. Within the formula (T_a) is the air temperature in degrees
Celsius and (V) is the wind speed in km/hr. A similar formula with different constant values 
can be used with temperatures in degrees Fahrenheit and wind speeds in miles/hr.

    WCI = 13.12 + (0.6215)*T_a - (11.37) * (V^0.16) + (0.3965) * T_a * (V^0.16)

Write a program that begins by reading the air temperature and wind speed from the user. 
Once these values have been read your program should display the wind chill index rounded 
to the closest integer.

"""

air_temp = float(input("Enter the air temperature: "))
wind_speed = float(input("Enter the wind speed: "))

index = 13.12 + ((0.6215) * air_temp) - ((11.37) * (wind_speed ** 0.16)) + ((0.3965) * air_temp * (wind_speed**0.16))

print("For air temperature of {} deg C and wind speed {} km/hr, expected wind chill index is {}.".format(air_temp,wind_speed,round(index,0)))