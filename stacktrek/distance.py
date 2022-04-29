from cmath import sqrt


import math 
x1 = float(input("what is x1:"))
y1 = float(input("what is y1:"))
x2 = float(input("what is x2:"))
y2 = float(input("what is y2:"))

d =math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"{d:.2f}")