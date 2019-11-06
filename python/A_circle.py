#use math module to get the value of pi
from math import pi

#ask for radius
r = float(input ("Input the radius of the circle : "))

#print the area of circle
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
