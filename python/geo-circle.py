#Write a Python program to get the the volume of a sphere with radius
import math
pi = math.pi
r= float(input('Enter Radius:'))
V= 4.0/3.0*pi* r**3
A= pi*r**2
C=2*pi*r
print('The volume of the sphere is: ',V)
print('The Area of the Circle is: ',A)
print('The circumference of the Circle is: ',C)
